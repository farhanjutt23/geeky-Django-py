from django.shortcuts import render



# Create your views here.
def learn_django(request):
    return render(request,'course_one.html')
def learn_python(request):
    return render(request,'course_two.html')
