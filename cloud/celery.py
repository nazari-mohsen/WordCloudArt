import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloud.settings')
app = Celery('cloud')
app.config_from_object('django.conf:settings', namespace='CELERY')
#http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html
app.conf.broker_url = f"redis://:{os.environ.get('REDIS_PASSWORD', '')}@{os.environ.get('REDIS_HOST', 'redis')}:{os.environ.get('REDIS_PORT', '6379')}/3"
app.autodiscover_tasks()

