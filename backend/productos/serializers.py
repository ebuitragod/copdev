from rest_framework import serializers

from .models import Category, Consumption, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('code',
                  'name',
                 )

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('code',
                  'name',
                 )

class InformacionCategorySerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='get_code_display')

    class Meta:
        model = Category
        fields = ('code',
                  'name',
                 )

class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ('timestamp',
                  'product',
                  'quantity',
                 )

class PostConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ('timestamp',
                  'product',
                  'quantity',
                 )

class InformacionConsumptionSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='get_product_display')
    #timestamp = serializers.DateField(source='get_timestamp_display')

    class Meta:
        model = Consumption
        fields = ('timestamp',
                  'product',
                  'quantity',
                 )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code',
                  'name',
                  'category',
                 )

class PostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code',
                  'name',
                  'category',
                 )

class InformacionProductSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='get_code_display')
    name = serializers.CharField(source='get_name_display')

    class Meta:
        model = Product
        fields = ('code',
                  'name',
                  'category',
                 )
