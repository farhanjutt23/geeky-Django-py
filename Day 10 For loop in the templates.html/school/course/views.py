from django.shortcuts import render

# Create your views here.
def django_learing(self):
    student={'names':['Rahul','Farhan','Ali','Ahmad']}
    return render(self,'course/course_one.html', student)