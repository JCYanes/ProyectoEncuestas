from django.urls import path
from django.urls import include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('encuestas/', views.ListadoEncuestas.as_view(), name='listadoEncuesta'),
    #path('encuesta/<pk>', views.DetalleEncuesta.as_view(), name='encuesta-detalle'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)