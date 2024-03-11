import os
import time

from celery import Celery
from dotenv import load_dotenv


load_dotenv()

broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
backend_result_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1")
celery = Celery('tasks', broker=broker_url)

@celery.task(name='tasks.add')
def add(x, y):
    time.sleep(5)
    return x + y
