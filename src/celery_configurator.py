from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from dotenv import load_dotenv
from src.settings import INSTALLED_APPS


load_dotenv()

broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
backend_result_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1")

app = Celery('src')
app.config_from_object('src.settings', namespace='CELERY')
app.autodiscover_tasks(INSTALLED_APPS)
