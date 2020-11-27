from django import forms 
from .models import Category, Product, Consumption

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'code',
            'name',
        ]