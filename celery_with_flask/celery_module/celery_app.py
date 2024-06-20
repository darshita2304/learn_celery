from celery import Celery
from celery_module.celeryappconfig import CeleryAppConfig

app = Celery('celery_with_flask',
             broker=CeleryAppConfig.broker_url,
             backend=CeleryAppConfig.result_backend)

app.conf.update(
    result_expires=CeleryAppConfig.result_expires,
    task_annotations=CeleryAppConfig.task_annotations,
    celery_task_routes=CeleryAppConfig.task_routes
)

# Ensure Celery autodiscovers tasks
app.autodiscover_tasks(['celery_with_flask'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if __name__ == '__main__':
    app.start()