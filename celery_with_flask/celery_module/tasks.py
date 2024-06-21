from celery import chain
from .celery_app import app

# asyncronous task defination...


@app.task(name='celery_with_flask.celery_module.tasks.addition')
def addition(x, y):
    return x + y

# asyncronous task defination...


@app.task(name='celery_with_flask.celery_module.tasks.reverse')
def reverse(s):
    return s[::-1]


@app.task(name='celery_with_flask.celery_module.tasks.task1')
def task1(t1=None):
    print(t1 + 'hello world')
    return t1[::-1]


@app.task(name='celery_with_flask.celery_module.tasks.task2')
def task2(t2=None):
    print(t2 + 'hello world')
    return t2 + 'hello world'


@app.task(name='celery_with_flask.celery_module.tasks.task3')
def task3(t3=None):
    print(t3 + 'hello world')
    return t3 + 'hello world'


@app.task(name='celery_with_flask.celery_module.tasks.task4')
def task4(t4=None):
    print(t4 + 'hello world')
    return t4 + 'hello world'
