from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.ImageField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=40)
    stupas=models.CharField(max_length=70)
    