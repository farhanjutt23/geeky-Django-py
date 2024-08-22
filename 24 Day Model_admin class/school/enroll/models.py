from django.db import models

# Create your models here.
class Student(models.Model):
    stuID = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=80)

    # def __str__(self):
    #     return self.stuname

