from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.CharField(max_length=80)
    srupass = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.stuname





