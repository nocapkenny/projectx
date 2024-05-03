from django.shortcuts import render
from tea.models import prepod, stud, faa, group, teoria
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.serializers import FileField, ModelSerializer

#----students
class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = stud
        fields = "__all__"
        
# class Stud2Serializer(serializers.ModelSerializer):
#     # prepods = serializers.PrimaryKeyRelatedField(queryset=prepod.objects.all(), many=True)
#     class Meta:
#         model = stud
#         fields = ["id", "name", "group"]
        
class StudViewSet(viewsets.ModelViewSet):
    queryset = stud.objects.all()
    serializer_class = StudSerializer

class StudList(generics.ListAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mail']   
    
#----prepods
class PrepodSerializer(serializers.ModelSerializer):
    # studs = Stud2Serializer(many = True, read_only = True)
    class Meta:
        model = prepod
        fields = "__all__"

class PrepodViewSet(viewsets.ModelViewSet):
    queryset = prepod.objects.all()
    serializer_class = PrepodSerializer

class PrepodList(generics.ListAPIView):
    queryset = prepod.objects.all()
    serializer_class = PrepodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mail']
    
#----
class TeoriaSerializer(serializers.ModelSerializer):
    file = FileField()
    class Meta:
        model = teoria
        fields = "__all__"
        
class TeoriaViewSet(viewsets.ModelViewSet):
    queryset = teoria.objects.all()
    serializer_class = TeoriaSerializer
       
class TeoriaList(generics.ListAPIView):
    queryset = teoria.objects.all()
    serializer_class = TeoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['predmet','group']
    
class FileDownloadView(APIView):
    serializer_class = TeoriaSerializer
    def get(self, request, pk):
        file_model = teoria.objects.get(pk=pk)
        serializer = self.serializer_class(file_model)
        response = FileResponse(file_model.file.read(), as_attachment=True)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_model.file.name)
        return response
    
#----
class FaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = faa
        fields = "__all__"

class FaaViewSet(viewsets.ModelViewSet):
    queryset = faa.objects.all()
    serializer_class = FaaSerializer

#----
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = group
        fields = "__all__"

class GroupViewSet(viewsets.ModelViewSet):
    queryset = group.objects.all()
    serializer_class = GroupSerializer


    