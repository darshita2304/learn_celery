from learn_celery.celeryappconfig import CeleryAppConfig
from celery import Celery

app = Celery('learn_celery',
             broker=CeleryAppConfig.broker_url,
             backend=CeleryAppConfig.result_backend)

app.conf.update(
    result_expires=CeleryAppConfig.result_expires,
    task_annotations=CeleryAppConfig.task_annotations,
    celery_task_routes=CeleryAppConfig.task_routes,
    beat_schedule={
        'add-every-10-seconds': {
            'task': 'learn_celery.tasks.addition',
            'schedule': 10.0,
            'args': (2, 2)
        },
    },
    timezone='UTC',
)

# Ensure Celery autodiscovers tasks
app.autodiscover_tasks(['learn_celery'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if __name__ == '__main__':
    app.start()
