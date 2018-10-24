from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class appconfig(AppConfig):
    name = 'app'
    verbose_name = _('app')

    def ready(self):
        import app.signals