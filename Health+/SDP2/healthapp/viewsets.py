from rest_framework import viewsets
from . import models
from . import serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = models.UserCreationForm.objects.all()
    serializer_class = serializers.UserSerializer
