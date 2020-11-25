import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now

from .product import Product

class Consumption(models.Model):
    timestamp = models.DateField('Timestamp', auto_created=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.SmallIntegerField(blank=False, null=False, default=1)

    class Meta:
        verbose_name = 'Consumición'
        verbose_name_plural = 'Consumiciones'