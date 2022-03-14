from django.db import models

# Create your models here.

class Component(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static')
    tag = models.CharField(max_length=50)
    code = models.TextField()
 
 