from __future__ import absolute_import, unicode_literals

from celery import Celery
from src.settings import INSTALLED_APPS

app = Celery('src')
app.config_from_object('src.settings', namespace='CELERY')
app.autodiscover_tasks(INSTALLED_APPS)
