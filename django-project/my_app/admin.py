from django.contrib import admin
from .models import Project, Task

# Este archivo admin se encarga de registrar los modelos de la aplicación
# Permirte administar todo el proyecto por ejemplo crear, editar, eliminar, etc.
# Este panel ya viene por defecto en django
# Desde aca se pueden agregar los modelos en el panel principal de admnistracion

admin.site.register(Project)
admin.site.register(Task)
