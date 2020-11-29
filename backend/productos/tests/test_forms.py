import datetime
import pandas as pd

from django.test import TestCase
from django.utils import timezone
from django.utils.encoding import force_text

from productos.models import Product, Category, Consumption
from productos.forms import ProductForm, CategoryForm, ConsumptionForm

class ProductFormTestCase(TestCase):
    def setUp(self):
        landline = Category.objects.create(
            code = 'LL',
            name = 'Landline',
        )
        mobile = Category.objects.create(
            code = 'MO',
            name = 'Mobile',
        )
        Product.objects.create(
         code = 'LL01',
         name = 'ADSL',
         category = Category.objects.get(code = 'LL'),
        )

class CategoryFormTestCase(TestCase):
    """
    Revisa si la API crea objetos en Categoria
    """
    def setUp(self):
        landline = Category.objects.create(
            code = 'LL',
            name = 'Landline',
        )
        mobile = Category.objects.create(
            code = 'MO',
            name = 'Mobile',
        )

    def test_valid_form(self):
        c = Category.objects.create(name='Category_form', code = 'TVF')
        data = {'code': c.code,
                'name': c.name,
                }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid)

    def test_valid_form(self):
        p = Product.objects.create(name='Prueba_form', code = 'TVF', category = Category.objects.get(code = 'LL'))
        data = {'code': p.code,
                'name': p.name,
                'category': p.category,
                }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid)

