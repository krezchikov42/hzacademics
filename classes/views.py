from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClassSerializer
from django.core import serializers
from .models import Class
from core.serializers import UserSerializer
import json
import logging

class ClassList(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if (request.user.is_authenticated):
            print('authed')
            print(request.user)
        serializer = ClassSerializer(Class.objects.all(), many=True)
        return Response({'items': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        request.data['user_id'] = request.user.id
        class_ = ClassSerializer(data=request.data)
        if class_.is_valid():
            class_.save()
            return Response(class_.data, status=status.HTTP_201_CREATED)
        logging.warning(f'Error creating Class: {class_.errors}')
        
        return Response(class_.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)