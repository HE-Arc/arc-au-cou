from urllib import response
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from arcaucouapp.models import Sudoku
from arcaucouapp import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from arcaucouapp.serializers import UserSerializer, SudokuSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SudokuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to get the sudoku of the day and to solve it.
    """
    queryset = Sudoku.objects.all()
    serializer_class = SudokuSerializer
    permission_classes = [permissions.IsAuthenticated]

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
        return Response({'result': sudoku.check_win(sudoku.end_sudoku)})
