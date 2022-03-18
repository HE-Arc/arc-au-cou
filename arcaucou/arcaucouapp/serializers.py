from django.contrib.auth.models import User, Group
from arcaucouapp.models import Sudoku
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SudokuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sudoku
        fields = ['url', 'start_sudoku', 'end_sudoku', 'date']
