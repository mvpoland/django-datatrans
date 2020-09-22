from django.db import models
from django.utils.translation import ugettext_lazy as _
from datatrans.utils import register


class Option(models.Model):
    name = models.CharField(_("name"), max_length=64)

    class Meta:
        verbose_name = _("option")
        verbose_name_plural = _("options")

    def __str__(self):
        return "{}".format(self.name)


class OptionTranslation:
    fields = ("name",)


register(Option, OptionTranslation)
