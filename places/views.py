from rest_framework import viewsets
from places import serializers
from places import models
# Create your views here.


class PlacesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlacesSerializer
    queryset = models.Places.objects.all()

