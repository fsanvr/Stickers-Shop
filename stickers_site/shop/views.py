from re import template
from django.shortcuts import render
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
    context = {

    }
    return HttpResponse(template.render(context, request))


def user_login(request):
    context = {}

    if request.user.is_authenticated:
        print('ты уже вошёл, молодец', request.user.username)
        return HttpResponseRedirect(reverse('index'))

    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('успешная авторизация')
            return HttpResponseRedirect(reverse('index'))
        else:
            context['error_message'] = form.errors
            print('ошибка авторизации')
    
    template = loader.get_template('shop/login.html')
    context['form'] = UserLoginForm()
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
    #print(context['form'])
    return HttpResponse(template.render(context, request))


#@login_required
#def profile(request):
#    template = loader.get_template('shop/profile.html')
#    context = {}
#
#    stickers = Stickers.objects.filter(username=request.user.username)
#    context['items'] = stickers
#    form = CreateStickerForm()
#    context['form'] = form
#
#    return HttpResponse(template.render(context, request))


@login_required
def profile(request):
    template = loader.get_template('shop/profile.html')
    context = {}
    
    if request.method == 'POST':
        form = CreateStickerForm(data=request.POST, files=request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            print('успешное добавление стикера пользователя', request.user.username)
            return HttpResponseRedirect(reverse('profile'))
        else:
            context['error_message'] = form.errors
            print(form.errors)


    context['stickers'] = Stickers.objects.filter(user=request.user)
    print(context['stickers'])
    context['form'] = CreateStickerForm()

    return HttpResponse(template.render(context, request))
        