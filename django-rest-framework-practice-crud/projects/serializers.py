## Los Serializadores son para convertir los datos de Django a JSON esto es para que el cliente pueda entender los datos al realizar las peticiones

from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')