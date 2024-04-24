from django.shortcuts import render
from tea.models import prepod, stud, faa, group, teoria
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse

#----students
class StudSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = stud
        fields = "__all__"

class Stud2Serializer(serializers.ModelSerializer):
    prepods = serializers.PrimaryKeyRelatedField(queryset=prepod.objects.all(), many=True)
    class Meta:
        model = stud
        fields = ["id", "name", "group", "prepods"]
        
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
    studs = Stud2Serializer(many = True, read_only = True)
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
    
# class DownloadFileFromDBView(APIView):
#     def get(self, request, tema):
#         file_obj = teoria.objects.get(tema=tema)
#         file_content = file_obj.docfile.read()  # Предполагается, что поле file_field хранит содержимое файла
#         response = HttpResponse(file_content, content_type='application/octet-stream')
#         response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_obj.tema)
#         return response
    
#----
class FaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = faa
        fields = "__all__"


class FaaViewSet(viewsets.ModelViewSet):
    queryset = faa.objects.all()
    serializer_class = FaaSerializer


#----
# class PrepodList(generics.ListAPIView):
#     serializer_class = PrepodSerializer
#     def get_queryset(self):
#         queryset = prepod.objects.all()
#         name = self.request.query_params.get('name')
#         if name is not None:
#             queryset = queryset.filter(prepod__name = name)
#         return queryset
    
# class Prr(django_filters.FilterSet):
#     class Meta:
#         model = prepod
#         fields = '__all__'  
    
# class PrepFilt(viewsets.ModelViewSet):
#     queryset = prepod.objects.all()
#     serializer_class = PrepodSerializer
#     filter_class = Prr
#     filter_backends = [DjangoFilterBackend]
    
    