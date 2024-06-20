from celery import Celery
from learn_celery.celeryappconfig import CeleryAppConfig

app = Celery('learn_celery',
             broker=CeleryAppConfig.broker_url,
             backend=CeleryAppConfig.result_backend)

app.conf.update(
    result_expires=CeleryAppConfig.result_expires,
    task_annotations=CeleryAppConfig.task_annotations,
    celery_task_routes=CeleryAppConfig.task_routes,
)

# Ensure Celery autodiscovers tasks
app.autodiscover_tasks(['learn_celery'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if __name__ == '__main__':
    app.start()
