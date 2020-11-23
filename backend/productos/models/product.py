import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now

from .category import Category

class Product(models.Model):
    code = models.CharField('Código del producto', max_length=10)
    name = models.CharField('Nombre', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return '({}): {} - {}'.format(self.name, self.category, self.name)

    class Meta:
        ordering = ['category', 'name', 'code']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        