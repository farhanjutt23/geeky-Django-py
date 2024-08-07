from django.shortcuts import render
from datetime import datetime
# Create your views here.
def django_learing(self):
      dta=datetime.now()
      return render(self,'course/course_one.html',{'dt ':dta})


