import csv, io 
import pandas as pd 

from django import forms
from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path

from .models import Category, Consumption, Product


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class ConsumptionInLine(admin.StackedInline):
    model = Consumption
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    change_list_template = 'admin_productos/product_changelist.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls
    
    def import_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES['csv_file']
            data_set = pd.read_csv(io.StringIO(csv_file.read().decode('UTF-8')), sep=',')
            data_set = data_set.fillna(0) 
            data_set['code'] = data_set['code'].astype(str)
            data_set['name'] = data_set['name'].astype(str)
            #data_set['category'] = data_set['category'].astype(str) #REVISSAR!

        for index, row in data_set.iterrows():
            Product.objects.update_or_create(
                code = row['code'],
                name = row['name'],
           #     category = row['category']
            )
        self.message_user(request, 'El seu csv ha estat importat.')
        return render(
            request, 'admin_productos/csv_form.html', payload
        )
    
    fieldsets = [
        (None,                  {'fields':[ 'code',
                                            'name',
                                            'category'
                                            ]
                                }
        )
    ]

    #list_display = ('category, name, code'),
    #readonly_fields = ()
    #list_filter = ('category')
    search_fields = ['category', 'name', 'code']

    inlines = [
        ConsumptionInLine,
    ]


@admin.register(Category)
class Category(admin.ModelAdmin):

    fieldsets = [
        (None,                  {'fields': [ 'code',
                                             'name',
                                            ]
                                }
        )
    ]

    list_display = ('code', 'name')
    #readonly_fields = ()
    #list_filter = ()
    search_fields = ['code', 'name']
    

