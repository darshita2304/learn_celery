from .celery_app import app


@app.task(name='learn_celery.tasks.addition')
def addition(x, y):
    return x + y
