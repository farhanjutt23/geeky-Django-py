from django.shortcuts import render

# Create your views here.
def learn_django(self):
    return render(self,'course/course_one.html',{'nm': "djano course"} )
