from django.apps import AppConfig

# Este archivo apps viene siendo como el archivo settings de la aplicación
# Aqui se registran las aplicaciones que se van a usar en el proyecto
# Aqui se  registra el nombre de la aplicación

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'
