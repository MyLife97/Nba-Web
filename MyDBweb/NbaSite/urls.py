from django.urls import path

from . import views

app_name = 'NbaSite'

urlpatterns = [
    path('', views.home, name='home'),	
]