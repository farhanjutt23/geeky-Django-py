from django.shortcuts import render

# Create your views here.
def django_fee(self):
    return render(self, 'fee/fee_one.html',{'tit': 'learn Django fee', 'cn': 'django fee'} )
    