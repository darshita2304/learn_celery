class CeleryAppConfig:
    # broker_url = 'pyamqp://darshita:darshita@localhost//'
    # result_backend = 'rpc://'
    broker_url = 'redis://localhost:6379/0'  # Redis as broker
    result_backend = 'redis://localhost:6379/0'  # Redis as result backend
    result_expires = 3600
    task_annotations = {'*': {'rate_limit': '10/s'}}
    task_ignore_result = False
    task_track_started = True
    enable_events = True
    result_cache_max = 1000
    task_routes = {
        'celery_module.tasks.addition': {'queue': 'default'},
        'celery_module.tasks.reverse': {'queue': 'default'},
        'celery_module.tasks.task1': {'queue': 'default'},
        'celery_module.tasks.task2': {'queue': 'default'},
        'celery_module.tasks.task3': {'queue': 'default'},
        'celery_module.tasks.task4': {'queue': 'default'}

    }
