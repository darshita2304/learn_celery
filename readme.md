## learn_celery is a module.. celery app is worker which runn celery app and having different tasks..
## to run the celery server/worker

celery -A learn_celery.celery_app worker -l info -P eventlet


# to assign task to celery app...
python main.py


### to run periodic tasks...
# to run server/worker
celery -A learn_celery.periodic_celery_app worker --loglevel=info

## to start 1st time beating...
celery -A learn_celery.periodic_celery_app beat --loglevel=info

