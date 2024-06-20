from datetime import datetime, timedelta
from celery_module.tasks import addition, reverse
from celery import chain
from time import sleep
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


if __name__ == '__main__':

    # ****************by default task running **************************
    # calling additon tasks asynchronously using delay()...
    result = addition.delay(4, 4)
    try:
        print('Task Result:', result.get(timeout=30))
    except Exception as e:
        print('Error rrrrrrrrrrr:', e)

    # ****************periodic task running **************************
   # Schedule the task to be executed 10 seconds from now
    result = addition.apply_async((6, 6), countdown=10)

    # Or schedule the task to be executed at a specific time
    eta = datetime.utcnow() + timedelta(seconds=5)
    result = addition.apply_async((5, 5), eta=eta)

    try:
        # Retrieve the result (will block until the result is ready)
        print('Periodic Task Result:', result.get(timeout=30))
    except Exception as e:
        print('Error rrrrrrrrrrr:', e)
