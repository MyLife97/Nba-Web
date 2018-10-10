from django.urls import path

from . import views

app_name = 'NbaSite'

urlpatterns = [
	#Home Page Pattern
    path('', views.home, name='home'),	
    #Search Pattern
    path('search_player=<str:player_name>/', views.search_by_name, name = 'search_by_name'),
    #Add Pattern
    path('add_player=<str:player_name>_team=<str:team>/', views.add_player, name = 'add_player'),
    #Delete Pattern
    path('delete_player=<str:player_name>/', views.delete_by_name, name = 'delete_by_name'),
    #Change Pattern
    path('change_player=<str:player_name>_team=<str:team>/', views.change_team_by_name, name = 'change_team_by_name'),

]