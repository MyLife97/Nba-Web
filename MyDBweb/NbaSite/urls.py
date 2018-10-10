from django.urls import path

from . import views

app_name = 'NbaSite'

urlpatterns = [
	#Home Page Pattern
    path('', views.home, name='home'),	
    #Search Pattern
    path(r'search\?player=<str:player_name>/', views.search_by_name, name = 'search_by_name'),
    #Add Pattern
    path('add?player=<str:player_name>&team=<str:team>/', views.add_player, name = 'add_player'),
    #Delete Pattern
    path('delete?player=<str:player_name>/', views.delete_by_name, name = 'delete_by_name'),
    #Change Pattern
    path('change?player=<str:player_name>&team=<str:team>/', views.change_team_by_name, name = 'change_team_by_name'),

]