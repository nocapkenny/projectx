from django.shortcuts import render
from tea.models import prepod, stud, faa, group, teoria
# Create your views here.
from rest_framework import routers, serializers, viewsets


#----
class PrepodSerializer(serializers.ModelSerializer):
    class Meta:
        model = prepod
        fields = "__all__"


class PrepodViewSet(viewsets.ModelViewSet):
    queryset = prepod.objects.all()
    serializer_class = PrepodSerializer


#----
class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = stud
        fields = "__all__"


class StudViewSet(viewsets.ModelViewSet):
    queryset = stud.objects.all()
    serializer_class = StudSerializer
    
    
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
    