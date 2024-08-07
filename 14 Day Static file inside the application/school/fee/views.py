from django.shortcuts import render

# Create your views here.
def django_fee(self):
    return render(self,'fee/fee_one.html' ,{ 'nm': 'django fee', 'du': "3 weeks has 4000"})
