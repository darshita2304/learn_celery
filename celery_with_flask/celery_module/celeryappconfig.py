class CeleryAppConfig:
    broker_url = 'pyamqp://darshita:darshita@localhost//'
    result_backend = 'rpc://'
    result_expires = 3600
    task_annotations = {'*': {'rate_limit': '10/s'}}
    task_routes = {
        'celery_module.tasks.addition': {'queue': 'default'},
        'celery_module.tasks.reverse': {'queue': 'default'}
    }
