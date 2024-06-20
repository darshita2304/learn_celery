from celery import Celery
import celeryconfig

app = Celery('learn_celery',
             celeryconfig=celeryconfig)

app.conf.update(
    result_expires=3600,
)

# Ensure Celery autodiscovers tasks
app.autodiscover_tasks(['learn_celery'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


if __name__ == '__main__':
    app.start()
