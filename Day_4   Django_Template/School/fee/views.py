from django.shortcuts import render



# Create your views here.
def django_fee(request):
    return render(request,'fee_one.html')
def python_fee(request):
    return render(request,'fee_two.html')
