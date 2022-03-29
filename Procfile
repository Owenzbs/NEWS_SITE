web: gunicorn mysite.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
heroku ps:scale web=1
manage.py migrate
web: gunicorn --bind 0.0.0.0:8000 