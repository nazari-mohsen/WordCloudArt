from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from .models import Category


@receiver(post_save, sender=Category, dispatch_uid="Write issued")
@receiver(post_delete, sender=Category, dispatch_uid="Write issued")
def invalidate_cache_Config(sender, instance, **kwargs):
    cache.delete('category')
