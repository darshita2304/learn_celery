from datetime import datetime, timedelta
from learn_celery.tasks import addition, reverse
from celery import chain, group, chunks
from time import sleep
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


if __name__ == '__main__':

    # *********************** chaining, grouping task running *********************

    # Chain two tasks together
    # You can chain tasks to run them sequentially... 1st methods output will be forwarded to 2nd method as 1st arguments
    result = chain(addition.s(6, 6), addition.s(6)).apply_async()

    # Retrieve the result of the final task in the chain
    try:
        # Retrieve the result (will block until the result is ready)
        print('Group Task Result:', result.get(timeout=30))
    except Exception as e:
        print('Error rrrrrrrrrrr:', e)

    # Group multiple tasks to run in parallel
    result = group(addition.s(i, i) for i in range(10)).apply_async()
    # Retrieve the results of all tasks in the group
    print('Group Results:', result.get(timeout=30))
