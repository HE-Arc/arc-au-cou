from urllib import response
from django.shortcuts import render
from django.contrib.auth.models import User
from arcaucouapp.models import Sudoku, Group
from arcaucouapp import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from arcaucouapp.serializers import UserSerializer, SudokuSerializer, GroupSerializer

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
        user_logged = authenticate(
            username=user['username'], password=user['password'])
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
            return Response({"username": "{}".format(user_registered.username)})
        except:
            error['username'] = serializer.errors['username'][0]
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class SudokuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to get the sudoku of the day and to solve it.
    """
    queryset = Sudoku.objects.all()
    serializer_class = SudokuSerializer

    @action(detail=False)
    def generate_sudoku(self, request, pk=1):
        """
        Debug function used to generate a new sudoku
        Never to be used normally, the sudoku is generated daily at midnight (will be removed)
        """
        sudoku = Sudoku.objects.get(pk=pk)
        sudoku.generate()
        sudoku.save()
        return Response({'Sudoku': 'Sudoku generated at ' + sudoku.date.strftime("%d/%m/%Y, %H:%M:%S")})

    @action(detail=False)
    def get_sudoku(self, request):
        """
        Give the sudoku of the day to the user
        """
        sudoku = Sudoku.objects.get(pk=1)
        return Response({'sudoku': sudoku.format(),
                         'date': sudoku.date})

    @action(detail=False)
    def check_sudoku(self, request):
        """
        Verify if the user has correctly completed the sudoku
        """
        sudoku = Sudoku.objects.get(pk=1)
        # Need to be replaced by the user sudoku and a check for the time needs to be done
        return Response({'result': sudoku.check_win(request.data['sudoku'])})
