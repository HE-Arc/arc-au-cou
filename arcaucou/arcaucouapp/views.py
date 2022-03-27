from django.contrib.auth.models import User
from arcaucouapp.models import Sudoku, Group, Leaderboard, UserToGroup
from arcaucouapp.serializers import UserSerializer, SudokuSerializer, GroupSerializer, UserToGroupSerializer, GroupListSerializer, LeaderboardSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.    
class GroupViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action == 'list':
            return GroupListSerializer
        return GroupSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = response.data
        group = Group.objects.get(name=instance['name'])
        token = request.META.get('HTTP_AUTHORIZATION')[6:]        
        user_id = Token.objects.get(key=token).user.id
        ids = {'user':user_id, 'group':group.id}
        serializer = UserToGroupSerializer(data=ids)
        if serializer.is_valid():
            user_to_group = serializer.save()
            if user_to_group is not None:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'failed':'User could not join group'},status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def joingroup(self, request):
        group_data = request.data
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        user_id = Token.objects.get(key=token).user.id
        group = Group.objects.get(name=group_data['name'])
        print(check_password(group_data['password'],group.password))
        if group is not None and check_password(group_data['password'],group.password):
            try:
                user_to_group = UserToGroup.objects.get(user=user_id, group=group.id)
            except UserToGroup.DoesNotExist:
                user_to_group = None
            if user_to_group is not None:
                return Response({'failed':'User is already in group'},status=status.HTTP_400_BAD_REQUEST)
            ids = {'user':user_id, 'group':group.id}
            serializer = UserToGroupSerializer(data=ids)
            if serializer.is_valid():
                user_to_group = serializer.save()
                if user_to_group is not None:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response({'failed':'User could not join group'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'failed':'Given data is not of a valid format'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'failed':'The group does not exist or the password is wrong'},status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def leavegroup(self, request):
        group_data = request.data
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        user_id = Token.objects.get(key=token).user.id
        group = Group.objects.get(name=group_data['name'])
        if group is not None:
            try:
                user_to_group = UserToGroup.objects.get(user=user_id, group=group.id)
            except UserToGroup.DoesNotExist:
                user_to_group = None
            if user_to_group is not None:
                user_to_group.delete()
                try:
                    user_to_group = UserToGroup.objects.get(group=group.id)
                except UserToGroup.DoesNotExist:
                    group.delete()
                except UserToGroup.MultipleObjectsReturned:
                    pass
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'failed':'The user is not part of the group'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'failed':'The group does not exist'},status=status.HTTP_400_BAD_REQUEST)
    
class LeaderboardViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [IsAuthenticated]
        
class LoginView(APIView):
    def post(self, request, format=None):
        user = request.data
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
            return Response({"username" : "{}".format(user_registered.username)},status=status.HTTP_200_OK)
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
