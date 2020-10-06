from django.shortcuts import render
from django.views import generic

from .models import Encuesta
# Create your views here.


def index(request):
    """
        Función vista para la página inicio del sitio.
    """
    # Genera contador del total de encuestas
    num_encuestas = Encuesta.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_encuestas': num_encuestas}
    )

"""
def ListadoEncuestas(request):
    listadoEncuestas = Encuesta.objects.all()
    return render(
        request,
        'listado_encuesta.html',
    context = {'num_encuestas':  listadoEncuestas}
    )

"""


class ListadoEncuestas(generic.ListView):
    model = Encuesta



