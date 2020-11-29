import datetime

from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from rest_framework import viewsets, permissions, parsers, status
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer, InformacionCategorySerializer, PostCategorySerializer
from .forms import CategoryForm

from .models import Product
from .serializers import ProductSerializer, InformacionProductSerializer, PostProductSerializer
from .forms import ProductForm

from .models import Consumption
from .serializers import ConsumptionSerializer, InformacionConsumptionSerializer, PostConsumptionSerializer
from .forms import ConsumptionForm

#CRUD
def list_category_view(request):
    context = {}
    context['dataset'] = Category.objects.all()
    return render(request, 'category/list_view.html', context)

def detail_category_view(request, code):
    context = {}
    context['data'] = Category.objects.get(code=code)
    return render(request, 'category/detail_view.html', context)

def create_category_view(request):
    #dictionary for initial data with fields as keys
    context = {}
    #add the dictionary durin initializations
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'category/create_view.html', context)

def update_category_view(request, code):
    context = {}
    #Fetch the object related to passed code (id)
    obj = get_object_or_404(Category, code = code)
    
    #pass the object as instance in form
    form = CategoryForm(request.POST or None, instance = obj)

    # save the data from the form  and redirecct to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('categoria/code=' + code + '/')
    
    #add form dictionary to context
    context['form'] = form
    
    return render(request, 'category/update_view.html', context)

def delete_category_view(request, code):
    context = {}
    obj = get_object_or_404(Category, code = code)
    if request.method == 'POST':
        #delete object
        obj.delete()
        #after deleting redirect to 
        #homepage
        return HttpResponseRedirect('category/lista/')
    return render(request, 'category/delete_view.html', context)


def list_product_view(request):
    context = {}
    context['dataset'] = Product.objects.all()
    return render(request, 'product/list_view.html', context)

def detail_product_view(request, code):
    context = {}
    context['data'] = Product.objects.get(code=code)
    return render(request, 'product/detail_view.html', context)

def create_product_view(request):
    #dictionary for initial data with fields as keys
    context = {}
    #add the dictionary durin initializations
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'product/create_view.html', context)

def update_product_view(request, code):
    context = {}
    #Fetch the object related to passed code (id)
    obj = get_object_or_404(Product, code = code)
    
    #pass the object as instance in form
    form = ProductForm(request.POST or None, instance = obj)

    # save the data from the form  and redirecct to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('producto/code=' + code + '/')
    
    #add form dictionary to context
    context['form'] = form
    
    return render(request, 'product/update_view.html', context)

def delete_product_view(request, code):
    context = {}
    obj = get_object_or_404(Product, code = code)
    if request.method == 'POST':
        #delete object
        obj.delete()
        #after deleting redirect to 
        #homepage
        return HttpResponseRedirect('producto/lista/')
    return render(request, 'product/delete_view.html', context)


def list_consumption_view(request):
    context = {}
    context['dataset'] = Consumption.objects.all()
    return render(request, 'consumption/list_view.html', context)

def detail_consumption_view(request, code):
    context = {}
    context['data'] = Consumption.objects.get(code=code)
    return render(request, 'consumption/detail_view.html', context)

def create_consumption_view(request):
    #dictionary for initial data with fields as keys
    context = {}
    #add the dictionary durin initializations
    form = ConsumptionForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'consumption/create_view.html', context)

def update_consumption_view(request, timestamp):
    context = {}
    #Fetch the object related to passed timestamp (id)
    obj = get_object_or_404(Consumption, timestamp = timestamp)
    
    #pass the object as instance in form
    form = ConsumptionForm(request.POST or None, instance = obj)

    # save the data from the form  and redirecct to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('consumision/timestamp=' + timestamp + '/')
    
    #add form dictionary to context
    context['form'] = form
    
    return render(request, 'consumption/update_view.html', context)

def delete_consumption_view(request, timestamp):
    context = {}
    obj = get_object_or_404(consumption, timestamp = timestamp)
    if request.method == 'POST':
        #delete object
        obj.delete()
        #after deleting redirect to 
        #homepage
        return HttpResponseRedirect('categoria/lista/')
    return render(request, 'categoria/delete_view.html', context)


#timestamp




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
