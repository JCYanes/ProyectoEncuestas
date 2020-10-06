from django.shortcuts import render
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from encuestas.models import Encuesta
from .serializers import SurveySerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

"""

@api_view(['GET', 'POST'])
def lista_encuesta(request):
    
    Método para listar encuestas o crear una nueva

   
    if request.method == 'GET':
        encuesta = Encuesta.objects.all()
        serializer = SurveySerializer(encuesta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_encuesta(request, pk):
   
        Método para obtener editar y borrar una encuesta en especifico

    
    try:
        encuesta = Encuesta.objects.get(pk=pk)
    except Encuesta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SurveySerializer(encuesta)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = SurveySerializer(encuesta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        encuesta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

"""
"""
class EncuestaArreglo(APIView):
   
    Listar todas las encuestas o crear una
    
    def get(self, request, format=None):
        survey = Encuesta.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EncuestaDetalles(APIView):
   
    Obtener, actualizar o borrar una encuesta
 

    def get_object(self, pk):
        try:
            return Encuesta.objects.get(pk=pk)
        except Encuesta.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        encuesta = self.get_object(pk)
        serializer = SurveySerializer(encuesta)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        encuesta = self.get_object(pk)
        serializer = SurveySerializer(encuesta, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        encuesta = self.get_object(pk)
        encuesta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class SurveyList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    Listar todas las encuestas y crear una nueva
    
    encuestas = Encuesta.objects.all() #Método del modelo Encuesta
    serializer_class = SurveySerializer
"""
"""
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""


class SurveyMixin(object):
    queryset = Encuesta.objects.all() #Tiene que llamarse queryset
    serializer_class = SurveySerializer


class EncuestaArreglo(SurveyMixin, ListCreateAPIView):
    pass


class EncuestaDetalles(SurveyMixin, RetrieveUpdateDestroyAPIView):
    pass
