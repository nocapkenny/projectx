from django.db import models

class faa(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name


class group(models.Model):
    name = models.CharField(max_length=15)
    faculty = models.ForeignKey(faa,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name


class prepod(models.Model):
    name = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length = 150, null = True)
    password = models.CharField(max_length = 100, null = True)
    type = models.CharField(max_length = 100, null = True)
    faculty = models.ForeignKey(faa,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class stud(models.Model):
    name = models.CharField(max_length=100, null=True)
    mail = models.CharField(max_length = 15, null = True)
    password = models.CharField(max_length = 100, null = True)
    type = models.CharField(max_length = 100, null = True)
    groupe = models.ForeignKey(group,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class teoria(models.Model):
    # PREDMET = (
    #     ('matan')
    # )
    tema = models.CharField(max_length=1000, null=True)
    prepodID = models.IntegerField(null = True)
    predmet = models.CharField(max_length = 100, null=True)
    file = models.FileField(upload_to="files", null = True)
    group = models.CharField(max_length = 1500, null=True)
    type = models.CharField(max_length = 100, null = True)
    def __str__(self):
        return self.group




