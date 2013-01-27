# Gif HQ  
_01.26.13_

This is a silly project with the silly intention of making a simple database that lets one store and share fantastic gifs from varying locations around the internets.


Requirements
---

This app requires the following packages:

- Django
- South
- gunicorn
- psycopg2
- wsgiref

But you can just install everything with Pip like so:

    pip install -r requirements.txt


Deploying
---

This app is meant to be run in production via Supervisor, Gunicorn, and Nginx. To do so, follow these here steps:

__Make a virtualenv for the app__

    virtualenv venv --distribute && source ./venv/bin/activate # "deactivate" to turn it off

__Install all the packages via pip__

    pip install -r requirements.txt

_Note: this app was built for use with Postgres as the database.  If you have another db flavor in mind, just switch that out of `requirements.txt` or else it will likely get mad at you during installation._

__Set up the database__

    ./manage.py syncdb

__Run a South migration (if needed)__

    ./manage.py migrate gifhq

_Note: you will probably want to update `supervisord.conf` to point at gunicorn_django in the virtualenv, not the global one_

__Collect the Django static assets__

    ./manage.py collectstatic

__Fire up Supervisord__

    supervisord -c supervisord.conf

__If desired, start/stop Supervisor__

    supervisorctl reread
    supervisorctl update
    supervisor stop gif
    supervisor start gif

That's it!


