from rest_framework import routers
from rest_framework.authtoken import views as authviews

from django.urls import include, path

# from .views import Estudios, InformacionEstudio
# from .views import Cuestionarios, InformacionCuestionario
# from .views import Preguntas, InformacionPregunta
# from .views import Elecciones, InformacionEleccion
# from .views import Etiquetas, InformacionEtiqueta

urlpatterns = [
    path('auth/', authviews.obtain_auth_token),
#     path('productos/', Estudios.as_view(), name='municipios'),
#     path('informacion_estudios/id_estudio=<str:id_estudio>/', InformacionEstudio.as_view(), name='informacion_estudio'),
#     path('cuestionarios/', Cuestionarios.as_view(), name='cuestionarios'),
#     path('informacion_cuestionarios/id_cuestionario=<str:id_cuestionario>/', InformacionCuestionario.as_view(), name='informacion_cuestionario'),
#     path('preguntas/', Preguntas.as_view(), name='preguntas'),
#     path('informacion_preguntas/id_pregunta=<str:id_pregunta>/', InformacionPregunta.as_view(), name='informacion_pregunta'),
#     path('elecciones/', Elecciones.as_view(), name='elecciones'),
#     path('informacion_elecciones/id_eleccion=<str:id_eleccion>/', InformacionEleccion.as_view(), name='informacion_eleccion'),
#     path('etiquetas/', Etiquetas.as_view(), name='etiquetas'),
#     path('informacion_etiquetas/id_etiqueta=<str:id_etiqueta>/', InformacionEtiqueta.as_view(), name='informacion_etiqueta'),
]