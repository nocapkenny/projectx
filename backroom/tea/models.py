from django.db import models
from rest_framework.reverse import reverse
from rest_framework.views import APIView


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
    
    def __str__(self):
        return self.name


class teoria(models.Model):
    name = models.CharField(max_length = 100)
    text = models.CharField(max_length = 5000)
    docfile = models.FileField(null=True)
    def __str__(self):
        return self.name