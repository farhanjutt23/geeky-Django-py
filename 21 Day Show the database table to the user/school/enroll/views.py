from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def Studentinfo(self):
  stud= Student.objects.all()
  return render(self,'enroll/student.html', {'stu':stud})
