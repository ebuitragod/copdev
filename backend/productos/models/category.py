import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Category(models.Model):
    code = models.CharField('Código', max_length=10, blank=False, null=False)
    name = models.CharField('Nombre de la categoría', max_length=100, blank=False, null=False, )