import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Category(models.Model):
    CODE = [
        ('LL', 'LL - Landline'),
        ('MO', 'MO - mobile'),
    ]

    code = models.CharField('Código', choices=CODE, max_length=2, blank=False, null=False, editable=False)
    name = models.CharField('Nombre', max_length=50,  blank=True, null=True, editable=False, unique=True)

    def __str__(self):
        return '({}): {}'.format(self.code, self.name)
    
    class Meta:
        ordering = ['name', 'code']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

