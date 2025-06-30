## Los API o viewsets son para crear las rutas de la API y especificar los metodos que haran uso de los serializadores

from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Esto es para obtener todos los proyectos
    permission_classes = [permissions.AllowAny] # Esto es para permitir que cualquier persona pueda acceder a los datos
    serializer_class = ProjectSerializer # Esto es para serializar los datos

