import datetime

from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, permissions, parsers, status
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# from estudios_api.models import Estudio, Cuestionario, Pregunta, Eleccion, Etiqueta
# from estudios_api.serializers import EstudioSerializer, CuestionarioSerializer, PreguntaSerializer, EleccionSerializer, EtiquetaSerialiazer
# from estudios_api.serializers import InformacionEstudioSerializer, InformacionCuestionarioSerializer, InformacionPreguntaSerializer, InformacionEleccionSerializer, InformacionEtiquetaSerializer
# from estudios_api.serializers import PostEstudioSerializer, PostCuestionarioSerializer, PostPreguntaSerializer, PostEleccionSerializer, PostEtiquetaSerializer

# class Estudios(APIView):
#     def get(self, request):
#         estudios = Estudio.objects
#         serializer = EstudioSerializer(estudios, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PostEstudioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class InformacionEstudio(APIView):
#     permission_classes = (AllowAny,) #Cambiar por IsAuthenticated

#     def get(self, request, id_estudio):
#         estudio = Estudio.objects.get(id_estudio=id_estudio)
#         serializer = InformacionEstudioSerializer(estudio)
#         return Response(serializer.data)
