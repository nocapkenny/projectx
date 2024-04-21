from django.db import models
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.postgres.fields import ArrayField

class faa(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class group(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class prepod(models.Model):
    name = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length = 150, null = True)
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
    prepods = models.ManyToManyField(prepod,related_name="studs", blank = True)
    def __str__(self):
        return self.name


class teoria(models.Model):
    tema = models.CharField(max_length=1000, null=True)
    prepodID = models.IntegerField(null = True)
    predmet = models.CharField(max_length = 100, null=True)
    docfile = models.FileField(max_length = 500,null=True)
    group = models.CharField(max_length = 1500, null=True)
    type = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.tema

    
    
