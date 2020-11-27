from rest_framework import routers
from rest_framework.authtoken import views as authviews

from django.urls import include, path

from .views import Categorias, InformacionCategoria
from .views import list_category_view, detail_category_view, create_category_view, update_category_view, delete_category_view

from .views import Productos, InformacionProducto
from .views import Consumiciones, InformacionConsumicion

urlpatterns = [
    path('auth/', authviews.obtain_auth_token),
    path('categorias/', Categorias.as_view(), name = 'categorias'),
    path('informacion_categorias/code=<str:code>/', InformacionCategoria.as_view(), name = 'informacion_categoria'),
    path('productos/', Productos.as_view(), name = 'productos'),
    path('informacion_productos/code=<str:code>/', InformacionProducto.as_view(), name = 'informacion_producto'),
    path('consumiciones/', Consumiciones.as_view(), name = 'consumiciones'),
    path('informacion_consumiciones/code=<str:code>/', InformacionConsumicion.as_view(), name = 'informacion_conscategoriaumicion'),

    #for CRUD
    path('categoria/lista/', list_category_view),
    path('categoria/crear/', create_category_view),
    path('categoria/code=<str:code>/', detail_category_view),
    path('categoria/code=<str:code>/editar/', update_category_view),
    path('categoria/code=<str:code>/eliminar/', delete_category_view),


]
