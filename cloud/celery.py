import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloud.settings')
app = Celery('cloud')
app.config_from_object('django.conf:settings', namespace='CELERY')
#http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html
app.conf.broker_url = 'redis://:mohsen@127.0.0.1:6379/0'
app.autodiscover_tasks()

