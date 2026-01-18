from django.db import models

class registerr(models.Model):
    name=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)