from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404, JsonResponse
from .models import Player, Team
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

import json
import datetime
# Create your views here.



def home(request):
	return render(request, 'NbaSite/home.html')

def search_by_name(request, player_name):
	try:
		player = Player.objects.get(player_name = player_name)
		# content = request.POST.get('name')
		return HttpResponse("Team:" + str(player.team) + " Begin Date:" + str(player.begin_date))
	except Player.DoesNotExist:
		return HttpResponse("Player %s is Not in the Table!" % player_name)
	# return HttpResponse(player)

def delete_by_name(request, player_name):
	try:
		old_player = Player.objects.get(player_name = player_name)
		old_player.delete()
		# return HttpResponse("Delete Succeed.")
		return HttpResponse("Player %s has been deleted successfully." % player_name)
	except Player.DoesNotExist:
		return HttpResponse("Player %s is Not in the Table!" % player_name)

def change_team_by_name(request, player_name, team_name):
	try:
		player = Player.objects.get(player_name = player_name)
		try:
			new_team = Team.objects.get(team_name = team_name)
		except Team.DoesNotExist:
			new_team = Team(team_name = team_name)
			new_team.save()

		player.team = new_team
		player.save()
		return HttpResponse('Change %s\'s team succeed.' % player_name)
	except Player.DoesNotExist:
		return HttpResponse("Change Fail. Player %s is Not in the Table!" % player_name)

def add_player(request, player_name, begin_date = datetime.datetime.now(), team_name = ''):

	try:
		old_player = Player.objects.get(player_name = player_name)
		return HttpResponse("Player %s is already in the Table." %player_name)
	except Player.DoesNotExist:
		try:
			team = Team.objects.get(team_name = team_name)
		except Team.DoesNotExist:
			team = Team(team_name = team_name)
			team.save()
			new_player = Player(player_name = player_name, begin_date = begin_date, team = team)
			new_player.save()
			return HttpResponse("Player %s has been added into %s." %(player_name, team_name))
			# return HttpResponse("TeamNotFound")

	new_player = Player(player_name = player_name, begin_date = begin_date, team = team)
	new_player.save()
	return HttpResponse("Player %s has been added into %s." %(player_name, team_name))
	#return render(request, 'polls/detail.html', {'question': question})

	# return HttpResponse(player)

# def ajax_test(request):
# 	name = 'James'
# 	return JsonResponse(name, safe = False)	

# def ajax_test(request):
#     user_name = request.POST.get("username")
#     password = request.POST.get("password")
#     print(user_name, password)
#     # i += 1
#     return HttpResponse("i")