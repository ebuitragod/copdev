from django import forms 
from .models import Category, Product, Consumption

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'code',
            'name',
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'code',
            'name',
            'category',
        ]

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = [
            'timestamp',
            'product',
            'quantity',
        ]