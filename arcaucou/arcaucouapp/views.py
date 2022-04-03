import datetime
from django.contrib.auth.models import User
from arcaucouapp.models import Sudoku, Group, Leaderboard, UserToGroup
from arcaucouapp.serializers import UserSerializer, UserListSerializer, SudokuSerializer, GroupSerializer, UserToGroupSerializer, LeaderboardSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
import json
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.  
class UserViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    '''
    '''
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        try:
            user = Token.objects.get(key=token).user
        except User.DoesNotExist:
            user = None
        if user is not None:
            return Response({'user': {'username':user.username,'email':user.email}},status=status.HTTP_200_OK)
        return Response({'failed':'L\'utilisateur n\'existe pas'},status=status.HTTP_400_BAD_REQUEST)
        
class GroupViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        '''
        '''
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        user_id = Token.objects.get(key=token).user.id
        groups_id = UserToGroup.objects.filter(user=user_id).values('group')
        groups = Group.objects.filter(id__in=groups_id).values("name")
        groups_name = [x['name'] for x in groups]
        return Response(groups_name,status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = response.data
        group = Group.objects.get(name=instance['name'])
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        user_id = Token.objects.get(key=token).user.id
        ids = {'user': user_id, 'group': group.id}
        serializer = UserToGroupSerializer(data=ids)
        if serializer.is_valid():
            user_to_group = serializer.save()
            if user_to_group is not None:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'failed':'L\'utilisateur n\'a pas pu rejoindre le groupe'},status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def joingroup(self, request):
        group_data = request.data
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        user_id = Token.objects.get(key=token).user.id
        try:
            group = Group.objects.get(name=group_data['name'])
        except Group.DoesNotExist:
            group = None
        if group is not None and check_password(group_data['password'],group.password):
            try:
                user_to_group = UserToGroup.objects.get(
                    user=user_id, group=group.id)
            except UserToGroup.DoesNotExist:
                user_to_group = None
            if user_to_group is not None:
                return Response({'failed':'L\'utilisateur est déjà dans ce groupe'},status=status.HTTP_400_BAD_REQUEST)
            ids = {'user':user_id, 'group':group.id}
            serializer = UserToGroupSerializer(data=ids)
            if serializer.is_valid():
                user_to_group = serializer.save()
                if user_to_group is not None:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response({'failed':'L\'utilisateur n\'a pas pu rejoindre le groupe'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'failed':'Les informations données ne sont pas valides'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'failed':'Le groupe n\'existe pas ou le mot de passe est faux'},status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def leavegroup(self, request):
        group_data = request.data
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        user_id = Token.objects.get(key=token).user.id
        try:
            group = Group.objects.get(name=group_data['name'])
        except Group.DoesNotExist:
            group = None
        if group is not None:
            try:
                user_to_group = UserToGroup.objects.get(
                    user=user_id, group=group.id)
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
                return Response({'failed':'L\'utilisateur ne fait pas partie de ce groupe'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'failed':'Le groupe n\'existe pas'},status=status.HTTP_400_BAD_REQUEST)
    
class LeaderboardViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action == "list_group":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def list(self, request, *args, **kwargs):
        '''
        '''
        return Response(Leaderboard.objects.all().order_by('time').values("user__username","time","date"),status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def list_group(self, request, *args, **kwargs):
        '''
        '''
        group_data = request.data
        try:
            group = Group.objects.get(name=group_data['name'])
        except Group.DoesNotExist:
            group = None
        if group is not None:
            users_id = UserToGroup.objects.filter(group=group.id).values('user')
            print(users_id)
            return Response(Leaderboard.objects.filter(user__id__in=users_id).order_by('time').values("user__username","time","date"),status=status.HTTP_200_OK)
        return Response({'failed':'Le groupe n\'existe pas'},status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        '''
        '''
        leaderboard_data = request.data
        token = request.META.get('HTTP_AUTHORIZATION')[6:]
        user_id = Token.objects.get(key=token).user.id
        data_ = {'user':user_id,'time':leaderboard_data['time']}
        serializer = LeaderboardSerializer(data=data_)
        if serializer.is_valid():
            leaderboard = serializer.save()
            if leaderboard is not None:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'failed':'L\'entrée dans le leaderboard n\'a pas pu être faite'},status=status.HTTP_400_BAD_REQUEST)
        if serializer.errors['non_field_errors'][0].code == 'unique':
            return Response({'failed':'Le joueur a déjà joué aujourd\'hui'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'failed':'Les données ne sont pas valides'},status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    def post(self, request, format=None):
        user = request.data
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
            error["password"] = "Les mots de passe ne correspondent pas."
        if serializer.is_valid():
            user_registered = serializer.save()
        try:
            return Response({"username": "{}".format(user_registered.username)}, status=status.HTTP_200_OK)
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
        sudoku = None
        if not Sudoku.objects.filter(pk=1).exists():
            sudoku = Sudoku.objects.create(id=1,
                                           start_sudoku="", end_sudoku="", date=datetime.datetime.now())
            sudoku.generate()
            sudoku.save()
        else:
            sudoku = Sudoku.objects.get(pk=1)
        return Response({'sudoku': sudoku.format(json.loads(sudoku.start_sudoku)),
                         'date': sudoku.date})

    @action(detail=False, methods=['post'])
    def check_sudoku(self, request):
        """
        Verify if the user has correctly completed the sudoku
        """
        sudoku = Sudoku.objects.get(pk=1)
        return Response({'result': sudoku.check_win(request.data['sudoku'])})
