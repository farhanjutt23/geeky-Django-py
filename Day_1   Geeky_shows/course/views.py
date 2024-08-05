from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(self):
    return HttpResponse('<h1> Farhan </h1>')   

'''Now we will create the url name of this in the url file'''
