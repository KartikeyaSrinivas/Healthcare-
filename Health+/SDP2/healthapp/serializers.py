from rest_framework import serializers
from .models import UserCreationForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreationForm
        fields = '__all__'
   