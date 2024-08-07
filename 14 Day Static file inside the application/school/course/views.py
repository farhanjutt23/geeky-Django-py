from django.shortcuts import render

# Create your views here.
def django_learing(self):
    return render(self,'course/course_one.html', { 'nm': 'django', 'du': "3 weeks"} )