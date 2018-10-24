from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PhotographyConfig(AppConfig):
    name = 'photography'
    verbose_name = _('photography')

    def ready(self):
        import photography.signals
