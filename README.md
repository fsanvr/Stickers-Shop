# STICKERS--SITE

# project description

this project is written as part of a course work, the goal is to learn frontend and backend development at a basic level. the site is a sticker store, with some flaws (in particular, it is impossible to buy something in this store)

# used in the project

* Django (framework)
* sqlite (database)
* heroku (host)
* html5 (base)
* css -grid (style)
* different libraries (for more information in requirements.txt )


# copy project

on your computer, it should be installed:

* Python 3.x.x
* Heroku CLI (and account on [heroku](https://heroku.com/))

open the folder where you want to download the project and follow these steps:

```bash
python -m venv env
env\Scripts\activate


pip install django
pip install dj-database-url
pip install gunicorn
pip install psycopg2
pip install whitenoise


cd stickers_site
heroku create <or your name>
git init
heroku git:remote -a stickers_site <or your name>
git add .
git commit -m "something"
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open
```

after these steps, you can start the local server and have already launched the site

# at the end

this project should be considered precisely as mastering the basic principles of web development, a lot has not been completed or not done at all (for example, heroku deletes pictures when going into sleep mode, but I haven't fixed it), but... I think everything will be fine :D

I am happy already from the fact that you have entered this repository!