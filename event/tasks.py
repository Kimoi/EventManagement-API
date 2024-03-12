import os
from celery import shared_task
import time


@shared_task
def event_sleep_60():
    time.sleep(60)
    return 'Good morning'
