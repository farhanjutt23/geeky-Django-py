from django.shortcuts import render

# Create your views here.
def django_learing(self):
    cname='django'
    duration='4 weeks'
    django_details={'cn': cname, 'du': duration}
    return render(self,'course/course_one.html', django_details)