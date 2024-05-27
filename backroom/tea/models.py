# -*- coding: windows-1251 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class faa(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name


class osenki(models.Model):
    predmet_name = models.CharField(max_length=155)
    kt1 = models.IntegerField(default = 0)
    kt2 = models.IntegerField(default = 0)
    kt3 = models.IntegerField(default = 0)
    kt4 = models.IntegerField(default = 0)
    def __str__(self):
        return self.predmet_name


class group(models.Model):
    name = models.CharField(max_length=15)
    faculty = models.ForeignKey(faa,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    TYPE = (
        ('Student','Student'),
        ('Professor','Professor')
    )
    type = models.CharField(max_length = 100, choices = TYPE, null = True)
    faculty = models.ForeignKey(faa,on_delete=models.CASCADE, null=True)
    fiGroup = models.ForeignKey(group,on_delete=models.CASCADE, null=True)
    mark_table = models.ManyToManyField(osenki, related_name='stud', null = True, blank=True)
    def __str__(self):
        return self.email
    
@receiver(post_save, sender = User)
def create_osenki_for_new_student(sender, instance, created, **kwargs):
    if created and instance.type == "Student":
        osenki1 = osenki.objects.create(predmet_name='Математический анализ')
        osenki2 = osenki.objects.create(predmet_name='Дискретная математика')
        osenki3 = osenki.objects.create(predmet_name='Аналитическая геометрия')
        osenki4 = osenki.objects.create(predmet_name='Языки программирования')
        osenki5 = osenki.objects.create(predmet_name='Линейная лгебра')
        osenki6 = osenki.objects.create(predmet_name='Алгоритмы и структуры данных')
        osenki7 = osenki.objects.create(predmet_name='История России')
        instance.mark_table.add(osenki1, osenki2, osenki3,osenki4, osenki5, osenki6, osenki7)

class teoria(models.Model):
    tema = models.CharField(max_length=1000, null=True)
    prepodID = models.IntegerField(null = True)
    predmet = models.CharField(max_length = 100, null=True)
    file = models.FileField(upload_to="files", null = True)
    group = models.CharField(max_length = 1500, null=True)
    type = models.CharField(max_length = 100, null = True)
    def __str__(self):
        return self.group
    