from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('learndj/',views.learing_django),
   path('learnpy/',views.learing_python),
   
]