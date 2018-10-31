from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from .models import Config, version


@receiver(post_save, sender=Config, dispatch_uid="Write issued")
@receiver(post_delete, sender=Config, dispatch_uid="Write issued")
def invalidate_cache_Config(sender, instance, **kwargs):
    cache.delete('conf')

@receiver(post_save, sender=version, dispatch_uid="Write issued")
@receiver(post_delete, sender=version, dispatch_uid="Write issued")
def invalidate_cache_version(sender, instance, **kwargs):
    cache.delete('version')