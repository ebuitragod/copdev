import datetime
import pandas as pd

from django.test import TestCase
from django.utils import timezone
from django.utils.encoding import force_text

from productos.models import Product, Category, Consumption
from productos.forms import ProductForm, CategoryForm, ConsumptionForm

class ProductTestCase(TestCase):
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

    def test_products_save(self):
        productos = Product.objects.all()
        self.assertEqual(len(productos), 1)
    #Anadiendo tests
    def create_product(self, name = 'Holitas', code = 'LL0005', category = Category.objects.get(code='LL')):
        return Product.objects.create(name = name, code = code)

    def test_product_creation(self):
        p = self.create_product()
        self.assertTrue(isinstance(p, Product))


class CategoryTestCase(TestCase):
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
    def test_categories_save(self):
        categorias = Category.objects.all()
        self.assertEqual(len(categorias), 2)

    #Anadiendo tests
    def create_category(self, name = 'Category, prueba', code = 'LL'):
        return Category.objects.create(name = name, code = code)

    def test_product_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))

class ConsumptionTestCase(TestCase):
    def setUp(self):
        landline = Category.objects.create(
            code = 'LL',
            name = 'Landline',
        )
        mobile = Category.objects.create(
            code = 'MO',
            name = 'Mobile',
        )
        producto_1 = Product.objects.create(
            code = 'LL01',
            name = 'ADSL',
            category = Category.objects.get(code = 'LL'),
        )
        time = timezone.now()
        cons_1 = Consumption.objects.create(
            timestamp = time,
            product = producto_1,
            quantity= 3
        )
        timestamp = '1490195805'
        cons_2 = Consumption.objects.create(
            timestamp = pd.to_datetime(timestamp, unit='s')
        )
    def test_consumption_save(self):
        consumiciones = Consumption.objects.all()
        self.assertEqual(len(consumiciones), 2)