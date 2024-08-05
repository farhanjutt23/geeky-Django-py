from django.shortcuts import render

# Create your views here.
def learing_django(self):
    cname='django'
    duration='4 months'
    seats=10
    django_details={'nm':cname, 'du':duration , 'st':seats}
    return render(self,'course/course_one.html', django_details)
def learing_python(self):
    return render(self,'course/course_two.html')
