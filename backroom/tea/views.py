# -*- coding: windows-1251 -*-
from django.shortcuts import render
from tea.models import User, osenki, teoria, faa, group
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets, generics, permissions
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.serializers import FileField
from django.http import FileResponse
from django.http import HttpResponse, Http404
import logging
from wsgiref.util import FileWrapper

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer
import logging

logger = logging.getLogger(__name__)

class UTF8CharsetJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    
#----OSENKI

class OsenSerializer(serializers.ModelSerializer):
    class Meta:
        model = osenki
        fields = "__all__"
        
class OsenViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = osenki.objects.all()
    serializer_class = OsenSerializer
    
#--------RAZRESHENIA

class PrepodPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return False  # ��������� POST, PUT, PATCH � DELETE
        return True
    
#--------NEW_USER

class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        mark_table_data = validated_data.pop('mark_table')
        instance = User.objects.create_user(**validated_data)
        for mark_data in mark_table_data:
            # ������� ������� Osen � ��������� �� � �������������
            mark_data.objects.create(user=instance, **mark_data)
        return instance
    class Meta:
        mark_table = OsenSerializer(many=True, read_only=True)
        model = User
        fields = ('id', 'type', 'first_name', 'username', 'email', 'password', 'fiGroup', 'faculty', 'mark_table')

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,) 
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # def get_permissions(self):
    #     user = self.request.user
    #     if user.type == "Student":
    #         return [CustomPermission()]
    #     else:
    #         return [IsAuthenticatedOrReadOnly()]
    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)  
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response('success')
        else:
            return Response(serializer.errors)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'fiGroup']   

class UserSerializer(serializers.ModelSerializer):
    faculty = serializers.PrimaryKeyRelatedField(queryset=faa.objects.all(), required=False, allow_null=True)
    class Meta:
        model = User
        fields = ['email','first_name','type','faculty','fiGroup','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            type = validated_data['type'],
            faculty = validated_data['faculty'],
            fiGroup = validated_data['fiGroup']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#-------TEORIA|PRAKTIK

class TeoriaSerializer(serializers.ModelSerializer):
    file = FileField()
    class Meta:
        model = teoria
        fields = "__all__"
        
class TeoriaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = teoria.objects.all()
    serializer_class = TeoriaSerializer
       
class TeoriaList(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = teoria.objects.all()
    serializer_class = TeoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['predmet', 'group']
    
# class FileDownloadView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     serializer_class = TeoriaSerializer
#     def get(self, request, pk):
#         file_model = teoria.objects.get(pk=pk)
#         serializer = self.serializer_class(file_model)
#         response = FileResponse(file_model.file.read(), as_attachment=True)
#         response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_model.file.name)
#         return response
# class FileDownloadView(APIView):
#     def get(self, request, file_id):
#         file_obj = teoria.objects.get(id=file_id)
#         response = HttpResponse(file_obj.file, content_type='application/octet-stream')
#         response['Content-Disposition'] = f'attachment; filename="{file_obj.file.name}"'
#         return response
# class FileDownloadView(APIView):
#     def get(self, request, file_id):
#         try:
#             file_obj = teoria.objects.get(id=file_id)  # Убедитесь, что это правильная модель
#             file_path = file_obj.file.path  # Предположим, у вас есть поле `file` в модели

#             with open(file_path, 'rb') as f:
#                 response = HttpResponse(f.read(), content_type='application/octet-stream')
#                 response['Content-Disposition'] = f'attachment; filename="{file_obj.file.name}"'
#                 return response
#         except teoria.DoesNotExist:
#             raise Http404("File does not exist")
logger = logging.getLogger(__name__)

class FileDownloadView(APIView):
    def get(self, request, id, format=None):
        queryset = teoria.objects.get(id = id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response


#-------FACULTY

class FaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = faa
        fields = "__all__"

class FaaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = faa.objects.all()
    serializer_class = FaaSerializer
class FaaList(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = faa.objects.all()
    serializer_class = FaaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

#-------GROUPS

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = group
        fields = "__all__"

class GroupViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = group.objects.all()
    serializer_class = GroupSerializer

class GroupList(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['faculty']
