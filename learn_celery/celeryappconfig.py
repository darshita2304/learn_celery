class CeleryAppConfig:
    broker_url = 'pyamqp://darshita:darshita@localhost//'
    result_backend = 'rpc://'
    result_expires = 3600
    task_annotations = {'*': {'rate_limit': '10/s'}}
    task_routes = {
        'learn_celery.tasks.addition': {'queue': 'default'},
        'learn_celery.tasks.reverse': {'queue': 'default'}
    }
