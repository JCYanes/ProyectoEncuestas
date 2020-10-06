from django.contrib import admin
from .models import Encuesta
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Miusuario

#Para gestionar usuarios con nuestra clase Usuario.
admin.site.register(Miusuario, UserAdmin)



@admin.register(Encuesta)
class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'propietario', 'created', 'updated')