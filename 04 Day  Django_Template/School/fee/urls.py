from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('feedj/',views.django_fee),
   path('feepy/',views.python_fee),
   

]