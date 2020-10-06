from django.urls import path

from api.views import * #Importamos las funciones de un módulo
from api import views #Importamos las clases que están definidas

"""urlpatterns = [
    path('encuestas/', lista_encuesta, name='lista_encuesta'),
    path('encuestas/<pk>', detalle_encuesta, name='detalle_encuesta'),
    ]"""

urlpatterns = [
    path('encuestas/', views.EncuestaArreglo.as_view(), name='lista_encuesta'),
    path('encuestas/<pk>', views.EncuestaDetalles.as_view(), name='detalle_encuesta'),
    ]