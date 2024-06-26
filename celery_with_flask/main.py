from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
from tzlocal import get_localzone
from celery import Celery
from celery.result import AsyncResult
from time import sleep
import pytz
import sys
import os
import json
from flask import Flask, request, render_template
from celery_module.tasks import addition, reverse, task1, task2, task3, task4

from celery_module.celery_app import app as celery_app


app = Flask(__name__)

# app = Celery('celery_app')
# app.config_from_object('celery_module.celeryappconfig')

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
task_list = dict()


def convert_local_to_utc_datetime(date_string):
    # Get the local time zone using zoneinfo
    # Replace with your local timezone # Asia/Calcutta for india by default on our system
    local_timezone = get_localzone()
    date_format = "%Y-%m-%dT%H:%M"
    # Convert the string to a naive datetime object
    naive_date_time_obj = datetime.strptime(date_string, date_format)
    # Convert the naive datetime object to a timezone-aware datetime object in local time zone
    local_date_time_obj = naive_date_time_obj.replace(tzinfo=local_timezone)
    # Print the local timezone-aware datetime object
    print(f"Local timezone-aware datetime: {local_date_time_obj}")
    # Convert the local timezone-aware datetime object to UTC
    utc_date_time_obj = local_date_time_obj.astimezone(ZoneInfo("UTC"))

    # Print the UTC timezone-aware datetime object
    print(f"UTC timezone-aware datetime: {utc_date_time_obj}")
    return utc_date_time_obj


def create_celery_task(task_datetime, task_fn):
    print("creating task...")
    result = []
    if task_fn == "task1":
        print(task_datetime)
        task_args = ["t1"]
        result = task1.apply_async(kwargs=dict(t1='t1'), eta=task_datetime)
        print("task1 added")

    elif task_fn == "task2":
        task_args = ["t2"]
        result = task2.apply_async(kwargs=dict(t2='t2'), eta=task_datetime)
        print("task2 added")

    elif task_fn == "task3":
        task_args = ["t3"]
        result = task3.apply_async(kwargs=dict(t3='t3'), eta=task_datetime)
        print("task3 added")

    elif task_fn == "task4":
        task_args = ["t4"]
        result = task4.apply_async(kwargs=dict(t4='t4'), eta=task_datetime)
        print("task4 added")

    else:
        print(" task not define")
    return result


def update_json_records():
    lst = []
    for key, value in task_list.items():
        lst.append(key)
    # only task key need to be recorded...
    with open('./celery_module/task_list.json', 'w') as fp:
        json.dump(lst, fp)


@ app.route("/")
def hello_world():
    return render_template("index.html")


@ app.route("/addtask", methods=['POST'])
def addtask():
    task_name = request.form['task_name']
    task_time = request.form['task_datetime']  # current datetime
    task_datetime = convert_local_to_utc_datetime(
        task_time)  # converting in localtime to servertime
    task_fn = request.form['tasks_fn']

    result = create_celery_task(task_datetime, task_fn)

    task_obj = {"task_name": task_name,
                "task_datetime": task_time, "task_fn": task_fn, "status": "PENDING", "result": result}
    task_list[result.id] = task_obj

    # update_json_records()

    return render_template("index.html", task_list=task_list)


@ app.route('/list_tasks')
def list_tasks():
    return render_template("result.html", results=task_list)


@app.route('/pause_task', methods=['POST'])
def pause_task():
    task_id = request.form['task_id']

    result = task_list[task_id]['result']
    task_list[task_id]['status'] = "PAUSED"
    result.revoke()
    print("task is requested to pause.... name = ")
    # print(task_id)
    print(task_list[task_id]['task_name'])

    # update_json_records()

    return render_template("index.html", task_list=task_list)


@app.route('/resume_task', methods=['POST'])
def resume_task():
    old_task_id = request.form['task_id']

    old_task_datetime = task_list[old_task_id]['task_datetime']
    task_datetime = convert_local_to_utc_datetime(old_task_datetime)

    new_result = create_celery_task(
        task_datetime, task_list[old_task_id]['task_fn'])

    task_obj = {"task_name": task_list[old_task_id]['task_name'],
                "task_datetime": old_task_datetime, "task_fn": task_list[old_task_id]['task_fn'], "status": "PENDING", "result": new_result}

    del task_list[old_task_id]
    task_list[new_result.id] = task_obj

    # update_json_records()
    return render_template("index.html", task_list=task_list)


@app.route('/get_status_tasks', methods=['GET'])
def get_status_tasks():
    for key, value in task_list.items():
        print(key)
        result = AsyncResult(key, app=celery_app)
        print("--------")
        print(result.ready())
        # task_list[key]['status'] = result.status

        if result.status == "SUCCESS":
            task_list[key]['status'] = result.status

    return render_template("index.html", task_list=task_list)
    # return "checking result....


if __name__ == '__main__':
    # Get the result of the task
    app.run(host='127.0.0.1', port=3000)

    # check_for_result()
