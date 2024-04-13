from django.db import models
from rest_framework.reverse import reverse
from rest_framework.views import APIView
class faa(models.Model):
    name = models.CharField(max_length=15)


class group(models.Model):
    name = models.CharField(max_length=15)


class prepod(models.Model):
    name = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length = 15, null = True)
    password = models.CharField(max_length = 100, null = True)
    # faculty = models.ForeignKey(faa, blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length = 100, null = True)
    faculty = models.CharField(max_length = 100, null = True)
   

class stud(models.Model):
    name = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length = 15, null = True)
    password = models.CharField(max_length = 100, null = True)
    # faculty = models.ForeignKey(faa, blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length = 100, null = True)
    group = models.CharField(max_length = 100, null = True)



class teoria(models.Model):
    name = models.CharField(max_length = 100)
    text = models.CharField(max_length = 5000)
    docfile = models.FileField(null=True)
