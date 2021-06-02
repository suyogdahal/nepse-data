import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nepse_data.settings')
app = Celery('nepse_data')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()