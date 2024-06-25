from celery import chain
from .celery_app import app
import json
import time

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
    print(t1 + '1111111111111111111111111111111')
    return t1 + '111111111111111111111111111111'


@app.task(name='celery_with_flask.celery_module.tasks.task2')
def task2(t2=None):
    print(t2 + '22222222222222222222')
    return t2 + '222222222222222222222222222222'


@app.task(name='celery_with_flask.celery_module.tasks.task3')
def task3(t3=None):
    print(t3 + '3333333333333333333333333333333')
    return t3 + '33333333333333333333333333333333'


@app.task(name='celery_with_flask.celery_module.tasks.task4')
def task4(t4=None):
    print(t4 + '44444444444444444444444444444444')
    time.sleep(10)
    return t4 + '44444444444444444444444444444444'


# @app.task(name='celery_with_flask.celery_module.tasks.check_for_result')
# def check_for_result():
#     with open("./celery_module/task_list.json", 'r') as json_file:
#         first_char = json_file.read(1)
#         if not first_char:
#             return "no task found"
#         else:
#             json_file.seek(0)
#             tasks = json.load(json_file)

#             for key in tasks:
#                 result = app.AsyncResult(key)
#                 # Wait for the task to finish
#                 result.wait()
#                 # Get the result of the task
#                 print("Task finished")
#                 print(result.result)
#     return "checking result...."
