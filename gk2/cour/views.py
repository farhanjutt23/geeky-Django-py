from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learndj(self):
    return HttpResponse('hlo!! farhan')
def learnjs(self):
    return HttpResponse('hlo!! javascript coder')
def learnpy(self):
    return HttpResponse('hlo!! python coder')
def learjava(self):
    a='<h1> hlo!! java coder</h1>'
    return HttpResponse(a)
def name(self):
    a='farhan'
    return HttpResponse(f"hlo who are you {a}")


