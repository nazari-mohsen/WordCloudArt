from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .tasks import send_email_device_crash
from .models import Crash

@receiver(post_save, sender=Crash)
@receiver(post_delete, sender=Crash)
def post_save_device_crash(sender, instance, created, **kwargs):
    if created:
        message = str(instance.log)
        send_email_device_crash.delay(message)