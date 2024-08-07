# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('learn/',views.django_learing),
]
