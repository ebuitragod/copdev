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
        if request.method == "POST":
            #=====Subiendo el archivo=====
            csv_file = request.FILES["csv_file"]
            data_set = pd.read_csv(io.StringIO(csv_file.read().decode('UTF-8')), sep=',')
            data_set = data_set.fillna(0) 
            #=====Leyendo los datos====
            data_set['code'] = data_set['code'].astype(str)
            data_set['name'] = data_set['name'].astype(str)
            data_set['category'] = data_set['category'].astype(str)
            #=====Subiendo los datos=====
            for index, row in data_set.iterrows():
                Product.objects.update_or_create(
                    code = row['code'],
                    name = row['name'],
                    category = Category.objects.get(code = row['category']),
                )

            self.message_user(request, 'El seu csv ha estat importat.')
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin_productos/csv_form.html", payload
        )
    
    fieldsets = [
        (None,                  {'fields': ['code',
                                            'name',
                                            'category',
                                           ]
                                }
        )
    ]

    list_display = ('code', 'name', 'category')
    #readonly_fields = ()
    list_filter = ('category', 'name')
    search_fields = ['name', 'code']

    inlines = [
        ConsumptionInLine,
    ]

@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    change_list_template = 'admin_productos/consumption_changelist.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls
    
    def import_csv(self, request):
        if request.method == "POST":
            #=====Subiendo el archivo=====
            csv_file = request.FILES["csv_file"]
            data_set = pd.read_csv(io.StringIO(csv_file.read().decode('UTF-8')), sep=',')
            data_set = data_set.fillna(0) 
            #=====Leyendo los datos====
            data_set['timestamp'] = data_set['timestamp'].astype(int)
            data_set['product'] = data_set['product'].astype(str)
            data_set['quantity'] = data_set['quantity'].astype(int)
            #=====Subiendo los datos=====
            for index, row in data_set.iterrows():
                Consumption.objects.update_or_create(
                    timestamp =pd.to_datetime(row['timestamp'], unit='s'),
                    product =  Product.objects.get(code = row['product']),
                    quantity = row['quantity']
                )

            self.message_user(request, 'El seu csv ha estat importat.')
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin_productos/csv_form.html", payload
        )
    

    fieldsets = [
        (
            None,           {'fields':[
                                        'timestamp',
                                        'product',
                                        'quantity',
                                      ]
                            }
        )
    ]

    list_display = ('product', 'timestamp', 'quantity')
    #list_filter = ('product', 'timestamp', 'quantity')
    search_fields = ('product', 'timestamp')


# @admin.register(Category)
# class Category(admin.ModelAdmin):

#     fieldsets = [
#         (None,                  {'fields': [ 'code',
#                                              'name',
#                                             ]
#                                 }
#         )
#     ]

#     list_display = ('code', 'name')
#     readonly_fields = ()
#     list_filter = ()
#     search_fields = ['code', 'name']
        