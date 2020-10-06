from rest_framework import serializers
from encuestas.models import Encuesta


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = ('pregunta','propietario', 'active')