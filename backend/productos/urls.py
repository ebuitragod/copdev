from rest_framework import routers
from rest_framework.authtoken import views as authviews

from django.urls import include, path

from .views import Categorias, InformacionCategoria
from .views import list_category_view, detail_category_view, create_category_view, update_category_view, delete_category_view

from .views import Productos, InformacionProducto
from .views import list_product_view, detail_product_view, create_product_view, update_product_view, delete_product_view

from .views import Consumiciones, InformacionConsumicion
from .views import list_consumption_view, detail_consumption_view, create_consumption_view, update_consumption_view, delete_consumption_view


urlpatterns = [
    path('auth/', authviews.obtain_auth_token),
    path('categorias/', Categorias.as_view(), name = 'categorias'),
    path('informacion_categorias/code=<str:code>/', InformacionCategoria.as_view(), name = 'informacion_categoria'),
    path('productos/', Productos.as_view(), name = 'productos'),
    path('informacion_productos/code=<str:code>/', InformacionProducto.as_view(), name = 'informacion_producto'),
    path('consumiciones/', Consumiciones.as_view(), name = 'consumiciones'),
    path('informacion_consumiciones/code=<str:code>/', InformacionConsumicion.as_view(), name = 'informacion_conscategoriaumicion'),

    #==========for CRUD==========
    #===Category
    path('categoria/lista/', list_category_view),
    path('categoria/crear/', create_category_view),
    path('categoria/code=<str:code>/', detail_category_view),
    path('categoria/code=<str:code>/editar/', update_category_view),
    path('categoria/code=<str:code>/eliminar/', delete_category_view), #Arreglar
    #===Product
    path('producto/lista/', list_product_view),
    path('producto/crear/', create_product_view),
    path('producto/code=<str:code>/', detail_product_view),
    path('producto/code=<str:code>/editar/', update_product_view),
    path('producto/code=<str:code>/eliminar/', delete_product_view),
    #===Consumption
    path('consumicion/lista/', list_consumption_view),
    path('consumicion/crear/', create_consumption_view),
    path('consumicion/timestamp=<str:timestamp>/', detail_consumption_view),
    path('consumicion/timestamp=<str:timestamp>/editar/', update_consumption_view),
    path('consumicion/timestamp=<str:timestamp>/eliminar/', delete_consumption_view), 
]

