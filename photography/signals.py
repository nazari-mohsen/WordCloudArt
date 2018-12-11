from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from .models import thumbnail, photo_main, photo_Mask


@receiver(post_save, sender=thumbnail, dispatch_uid="Write issued")
@receiver(post_delete, sender=thumbnail, dispatch_uid="Write issued")
def invalidate_cache_photo(sender, instance, **kwargs):
    cache.delete('photo')
    cache.delete('photodevelop')
    cache.delete_pattern('photo_conf*')
    cache.delete_pattern('photo_main*')


@receiver(post_save, sender=photo_main, dispatch_uid="Write issued")
@receiver(post_delete, sender=photo_main, dispatch_uid="Write issued")
def invalidate_cache_photo_main(sender, instance, **kwargs):
    cache.delete_pattern('photo_conf*')

@receiver(post_save, sender=photo_Mask, dispatch_uid="Write issued")
@receiver(post_delete, sender=photo_Mask, dispatch_uid="Write issued")
def invalidate_cache_photo_Mask(sender, instance, **kwargs):
    cache.delete_pattern('photo_conf*')