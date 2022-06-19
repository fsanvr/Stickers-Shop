#from re import template
#from django.shortcuts import render
import os
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import *


# Create your views here.

def index(request):
    #print(request)
    template = loader.get_template('shop/index.html')
    context = {}

    context['stickers'] = Stickers.objects.all()
    return HttpResponse(template.render(context, request))


def user_login(request):
    context = {}

    if request.user.is_authenticated:
        print('ты уже вошёл, молодец', request.user.username)
        return HttpResponseRedirect(reverse('index'))

    
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                print('успешная авторизация')
                return HttpResponseRedirect(reverse('index'))
            else:
                context['error_message'] = form.errors
                print('ошибка авторизации')
        else:
            context['error_message'] = 'Пожалуйста включите cookies и попробуйте снова'
    
    template = loader.get_template('shop/login.html')
    context['form'] = UserLoginForm()
    request.session.set_test_cookie()
    return HttpResponse(template.render(context, request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    context = {}

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('успешная регистрация')
            return HttpResponseRedirect(reverse('login'))
        else:
            context['error_message'] = form.errors
            print('ошибка регистрации')

    template = loader.get_template('shop/register.html')
    context['form'] = UserRegisterForm()

    return HttpResponse(template.render(context, request))


@login_required
def my_profile(request):
    template = loader.get_template('shop/profile.html')
    context = {}
    
    if request.method == 'POST' and request.POST['_method'] == 'POST':
        form = CreateStickerForm(data=request.POST, files=request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            print('успешное добавление стикера пользователя', request.user.username)
            return HttpResponseRedirect(reverse('my_profile'))
        else:
            context['error_message'] = form.errors
            print(form.errors)

    
    elif request.method == 'POST' and request.POST['_method'] == 'DELETE':
        id = request.POST['sticker_id']
        sticker = (Stickers.objects.filter(pk=id).all())[0]
        
        print(sticker.image.path)
        try:
            os.remove(sticker.image.path)
        except:
            pass
        try:
            Stickers.objects.filter(pk=id).delete()
        except:
            pass
        
        return HttpResponseRedirect(reverse('my_profile'))
        

    context['stickers'] = Stickers.objects.filter(user=request.user)
    context['form'] = CreateStickerForm()
    context['username'] = request.user.username

    return HttpResponse(template.render(context, request))


def profile(request, username):
    template = loader.get_template('shop/profile.html')
    context = {}

    user = User.objects.filter(username=username)[0]
    context['stickers'] = Stickers.objects.filter(user=user)
    context['form'] = CreateStickerForm()
    context['username'] = username

    return HttpResponse(template.render(context, request))


def add_cart(request):

    if 'cart' not in request.session:
        request.session['cart'] = dict()

    sticker = Stickers.objects.filter(pk=request.POST['sticker_id']).first()

    if str(sticker.id) not in request.session['cart']:
        request.session['cart'][str(sticker.id)] = int(request.POST['number'])
    else:
        request.session['cart'][str(sticker.id)] += int(request.POST['number'])

    if request.session['cart'][str(sticker.id)] > 99:
        request.session['cart'][str(sticker.id)] = 99
    
    if request.session['cart'][str(sticker.id)] < 0:
        request.session['cart'][str(sticker.id)] = 0

    request.session.modified = True

    print('успешное добавление в корзину')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


def cart(request):
    template = loader.get_template('shop/cart.html')
    context = {}

    if 'cart' in request.session:
        stickers = Stickers.objects.filter(pk__in=request.session['cart'].keys())

        if len(stickers) != len(request.session['cart'].keys()):
            keys = list()
            for key in request.session['cart'].keys():
                if not Stickers.objects.filter(pk=key).first():
                    keys.append(key)
            for key in keys:
                del request.session['cart'][key]
            request.session.modified = True
            



        numbers = request.session['cart'].values()
        context['cart'] = dict(zip(stickers, numbers))


    return HttpResponse(template.render(context, request))


def del_cart(request):

    try:
        id = request.POST['sticker_id']
        del request.session['cart'][id]
        request.session.modified = True

        print('RETIRED')
    except:
        print('something wrong...')

    return HttpResponseRedirect(reverse('cart'))