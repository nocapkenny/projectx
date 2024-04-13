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
    type = models.CharField(max_length = 100, null = True)
    faculty = models.CharField(max_length = 100, null = True)
    
    def __str__(self):
        return self.name
   

class stud(models.Model):
    name = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length = 15, null = True)
    password = models.CharField(max_length = 100, null = True)
    type = models.CharField(max_length = 100, null = True)
    group = models.CharField(max_length = 100, null = True)
    # url_osen = models.URLField(max_length= 150,null = True)
    def __str__(self):
        return self.name
   


class teoria(models.Model):
    name = models.CharField(max_length = 100)
    text = models.CharField(max_length = 5000)
    docfile = models.FileField(null=True)

class osenITH(models.Model):
    mat_an = models.IntegerField()
    diskr_mat = models.IntegerField()
    an_gem = models.IntegerField()
    yaz_prog = models.IntegerField()
    alg = models.IntegerField()
    lin_al = models.IntegerField()
    