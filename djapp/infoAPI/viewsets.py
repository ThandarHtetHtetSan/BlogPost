from rest_framework import viewsets
from .import models
from . import serializers
class InfoViewSet(viewsets.ModelViewSet):
    queryset = models.Info.objects.all()
    serializer_class = serializers.InfoSerializer
