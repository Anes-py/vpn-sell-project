from django.db import models
from django.utils.text import gettext_lazy as _

class ServersLocations(models.Model):
    name = models.CharField(_("name"), max_length=155)
    ping = models.PositiveIntegerField(_("ping"))
    server_load = models.PositiveIntegerField(_("server load"))

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("name"), max_length=155)
    data_limit = models.PositiveIntegerField(_("data limit"), help_text=_("unlimited:0"))
    device_connections = models.PositiveIntegerField(_("device connections"), help_text=_("unlimited:0"))
    server_locations_count = models.PositiveIntegerField(_("server locations_count"))
    plan_link = models.URLField()
    plan_price = models.PositiveIntegerField(_("price"))

    def __str__(self):
        return self.name
