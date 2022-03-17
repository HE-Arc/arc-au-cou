from django.shortcuts import render
from arcaucouapp.models import User, Group
from rest_framework import viewsets, permissions
from arcaucouapp.serializers import UserSerializer, GroupSerializer, UserCreateSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]