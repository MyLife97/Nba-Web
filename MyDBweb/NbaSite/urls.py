from django.urls import path

from . import views

app_name = 'NbaSite'

urlpatterns = [
    path('', views.home, name='home'),	
    path('player=<str:player>/', views.search_by_name, name = 'search_by_name')
    #####
    # path('ajax_test', views.ajax_test, name = 'ajax_test'),
]