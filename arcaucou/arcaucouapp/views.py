from django.contrib.auth.models import User
from arcaucouapp.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from arcaucouapp.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [IsAuthenticated]
        
class LoginView(APIView):
    def post(self, request, format=None):
        user = request.data.get('user')
        user_logged = authenticate(username=user['username'], password=user['password'])
        try:
            return Response({"result" : "success", "username" : "{}".format(user_logged.username)})
        except:
            return Response({"result" : "failed", "error" : "Username or password incorrect"})
            
    
class RegisterView(APIView):
    def post(self, request, format=None):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if user['password'] != user['password2']:
            return Response({"result" : "failed", "password": "Password fields didn't match."})
        if serializer.is_valid(raise_exception=True):
            user_registered = serializer.save()
        try:
            return Response({"result" : "success", "username" : "{}".format(user_registered.username)})
        except:
            return Response({"result" : "failed"})
