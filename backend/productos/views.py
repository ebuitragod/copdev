import datetime

from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, permissions, parsers, status
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer, InformacionCategorySerializer, PostCategorySerializer
from .models import Product
from .serializers import ProductSerializer, InformacionProductSerializer, PostProductSerializer
from .models import Consumption
from .serializers import ConsumptionSerializer, InformacionConsumptionSerializer, PostConsumptionSerializer

#APIview
class Categorias(APIView):
    def get(self, request):
        categoria = Category.objects
        serializer = CategorySerializer(categoria, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InformacionCategoria(APIView):
    permission_classes = (AllowAny,) #Cambiar por IsAuthenticated

    def get(self, request, codigo_categoria):
        categoria = Category.objects.get(code=codigo_categoria)
        serializer = InformacionCategorySerializer(categoria)
        return Response(serializer.data)

class Productos(APIView):
    def get(self, request):
        producto = Product.objects
        serializer = ProductSerializer(producto, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InformacionProducto(APIView):
    permission_classes = (AllowAny,) #Cambiar por IsAuthenticated

    def get(self, request, code):
        producto = ProductSerializer.objects.get(code=code)
        serializer = InformacionProductSerializer(categoria)
        return Response(serializer.data)

class Consumiciones(APIView):
    def get(self, request):
        consumiciones = Consumption.objects
        serializer = ConsumptionSerializer(consumiciones, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostConsumptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InformacionConsumicion(APIView):
    permission_classes = (AllowAny,) #Cambiar por IsAuthenticated

    def get(self, request, code):
        consumicion = ConsumptionSerializer.objects.get(code=code)
        serializer = InformacionConsumptionSerializer(categoria)
        return Response(serializer.data)
