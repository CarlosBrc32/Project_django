from django.db import models

class familiar (models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    birth = models.DateField()
    tipo = models.CharField(max_length=30)