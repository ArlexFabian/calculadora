from django.db import models
from django import db
# Create your models here.

class Getoperacion(models.Model):
    operacion = models.CharField(max_length=100)
    