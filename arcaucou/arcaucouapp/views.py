from django.contrib.auth.models import User
from arcaucouapp.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from arcaucouapp.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status

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
    permission_classes = [IsAuthenticated]
        
class LoginView(APIView):
    def post(self, request, format=None):
        user = request.data
        print(user)
        user_logged = authenticate(username=user['username'], password=user['password'])
        if user_logged is not None:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    
class RegisterView(APIView):
    def post(self, request, format=None):
        user = request.data
        serializer = UserSerializer(data=user)
        error = {}
        if user['password'] != user['password2']:
            error["password"] = "Password fields didn't match."
        if serializer.is_valid():
            user_registered = serializer.save()
        try:
            return Response({"username" : "{}".format(user_registered.username)})
        except:
            error['username'] = serializer.errors['username'][0]
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
