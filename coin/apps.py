from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoinConfig(AppConfig):
    name = 'coin'
    verbose_name = _('coin')
