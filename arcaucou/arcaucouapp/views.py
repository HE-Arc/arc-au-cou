from django.shortcuts import render
from django.contrib.auth import get_user_model
from arcaucouapp import serializers
from arcaucouapp.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from arcaucouapp.serializers import UserSerializer, UserLoginSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class LoginView(APIView):
    def post(self, request, format=None):
        user = request.data.get('user')
        serializer = UserLoginSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_logged = serializer.save()
        try:
            return Response({"result" : "success", "username" : "{}".format(user_logged['username'])})
        except:
            return Response({"result" : "failed"})
            
    
class RegisterView(APIView):
    def post(self, request, format=None):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_registered = serializer.save()
        return Response({"result" : "success", "username" : "{}".format(user_registered.username)})