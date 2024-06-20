from celery import chain
from .celery_app import app

# asyncronous task defination...


@app.task(name='celery_module.tasks.addition')
def addition(x, y):
    return x + y


# asyncronous task defination...
@app.task(name='celery_module.tasks.reverse')
def reverse(s):
    return s[::-1]
