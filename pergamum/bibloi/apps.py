
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BibloiConfig(AppConfig):  # Our app config class
    name = 'pergamum.bibloi'
    verbose_name = _("Articles Database")
