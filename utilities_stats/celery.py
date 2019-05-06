import os
from celery import Celery

# Setting the Default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utilities_stats.settings')
app = Celery('utilities_stats')

# Using a String here means the worker will always find the configuration information
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
