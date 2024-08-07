# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('fee/',views.django_fee)
]
