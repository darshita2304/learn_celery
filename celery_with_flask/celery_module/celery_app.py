from celery import Celery
from celery_module.celeryappconfig import CeleryAppConfig


app = Celery('celery_module',
             broker=CeleryAppConfig.broker_url,
             backend=CeleryAppConfig.result_backend)

app.conf.update(
    result_expires=CeleryAppConfig.result_expires,
    task_annotations=CeleryAppConfig.task_annotations,
    celery_task_routes=CeleryAppConfig.task_routes,
    task_track_started=CeleryAppConfig.task_track_started,
    task_ignore_result=CeleryAppConfig.task_ignore_result,
    enable_events=CeleryAppConfig.enable_events,
    worker_max_tasks_per_child=CeleryAppConfig.result_cache_max
)

# Ensure Celery autodiscovers tasks
app.autodiscover_tasks(['celery_module'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if CeleryAppConfig.enable_events:
    app.conf.update(
        worker_send_task_events=True,
        task_track_started=True,
    )

if __name__ == '__main__':
    # app.conf.CELERY_TIMEZONE = 'UTC'
    # Inspect the current worker
    app.start()
