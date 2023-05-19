from infoAPI.viewsets import InfoViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register('info',InfoViewSet)