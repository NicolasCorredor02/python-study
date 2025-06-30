## Rest Framework tiene un modulo especial que crea todas las rutas basicas 

from rest_framework import routers, urlpatterns
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')


urlpatterns = router.urls