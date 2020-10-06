from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class Miusuario(AbstractUser):
    usuario_id = models.AutoField(primary_key=True)





class Encuesta(models.Model):
    propietario = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                null=True, blank=True, on_delete=models.SET_NULL)
    #titulo = models.CharField(max_length=50)
    pregunta = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    #METODOS


    def __str__(self):

        return f'Propietario: {self.propietario},pregunta: {self.pregunta},activo: {self.active},creado: {self.created},actualizado: {self.updated}'

    """
        # Metadata
        class Meta:
            ordering = ["updated"]
    """