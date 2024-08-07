from django.shortcuts import render

# Create your views here.
def fee_django(self):
    return render(self, 'fee/fee_one.html',{'nm': 'django fees'} )
