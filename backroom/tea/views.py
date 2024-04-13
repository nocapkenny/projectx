from django.shortcuts import render
from tea.models import prepod, stud, faa, group, teoria
# Create your views here.
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters


#----prepods
class PrepodSerializer(serializers.ModelSerializer):
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
    filterset_fields = ['name']
    
#----students
class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = stud
        fields = "__all__"

class StudViewSet(viewsets.ModelViewSet):
    queryset = stud.objects.all()
    serializer_class = StudSerializer

class StudList(generics.ListAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']   
    
#----
class TeoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = teoria
        fields = "__all__"


class TeoriaViewSet(viewsets.ModelViewSet):
    queryset = teoria.objects.all()
    serializer_class = TeoriaSerializer
    
#----
class FaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = faa
        fields = "__all__"


class FaaViewSet(viewsets.ModelViewSet):
    queryset = faa.objects.all()
    serializer_class = FaaSerializer
    
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
    
    