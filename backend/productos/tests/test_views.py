import datetime
import pandas as pd

from django.test import TestCase
from django.utils import timezone
from django.utils.encoding import force_text

from productos.models import Product, Category, Consumption
from productos.forms import ProductForm, CategoryForm, ConsumptionForm

 
class CategoryViewsTestCase(TestCase):
 
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

    def test_get_api_category_json(self):
        response = self.client.get('/api/categorias/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            force_text(response.content),
            [
                {'code': 'LL', 'name': 'Landline'}, 
                {'code': 'MO', 'name': 'Mobile'},
            ]
        )

class ProductViewsTestCase(TestCase):
    """
    Revisa si la API crea objetos en Product apropiadamente para Productos
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
        Product.objects.create(
         code = 'LL01',
         name = 'ADSL',
         category = Category.objects.get(code = 'LL'),
        )

    def test_get_api_product_json(self):
        response = self.client.get('/api/productos/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            force_text(response.content),
            [
                {'code': 'LL01', 'name': 'ADSL', 'category': 1}
            ]
        )
