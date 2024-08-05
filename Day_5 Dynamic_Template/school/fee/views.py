from django.shortcuts import render

# Create your views here.
def fee_django(self):
    return render(self,'fee/fee_one.html')
def fee_python(self):
    return render(self,'fee/fee_two.html')