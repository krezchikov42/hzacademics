from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Class
from core.serializers import UserSerializer


class ClassSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Class
        fields = '__all__'