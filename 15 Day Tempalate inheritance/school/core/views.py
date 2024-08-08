from django.shortcuts import render

# Create your views here.
def home(self):
    return render (self,'core/home.html')
def about(self):
    return render (self,'core/about.html')