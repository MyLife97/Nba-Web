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

import MySQLdb as mdb
# Create your views here.

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'change',
    'db': 'nba_database',
    # 'charset': 'utf8'
}
conn = mdb.connect(**config)

conn.autocommit(True)

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

ZERO = 0


#############################
#          Fuctions         #
#############################

def home(request):
	return render(request, 'NbaSite/home.html')

def search_by_name(request,player_name):
	try:
		db_name = 'nba_database'
		conn.select_db(db_name)

		table_name = 'nbasite_player'
		
		cursor.execute('SELECT * FROM %s where player_name=\'%s\'' %(table_name, player_name))

		try:
			player_info = cursor.fetchone()

			begin_date = player_info[1]
			team_name = player_info[2]

			return HttpResponse("Team:" + '%s' %(team_name) + " Begin Date:" + '%s' %(begin_date))

		except:
			print("Fetch Player Failed")
			raise()
	except:
		return HttpResponse("Player %s is Not in the Table!" % player_name)

def delete_by_name(request, player_name):
	try:
		db_name = 'nba_database'
		conn.select_db(db_name)

		table_name = 'nbasite_player'

		try:
			result = cursor.execute('DELETE from %s where player_name = \'%s\'' %(table_name, player_name))

			if(result == ZERO):
				raise()
			else:
				return HttpResponse("Player %s has been deleted successfully." % player_name)

		except:
			print("Player Not Found.")
			raise()

	except:
		return HttpResponse("Player %s is Not in the Table!" % player_name)

def add_player(requset, player_name, team_name, begin_date = datetime.date.today()):
	try:
		db_name = 'nba_database'
		conn.select_db(db_name)

		table_name = 'nbasite_player'

		player_exist = cursor.execute('SELECT * from %s where player_name = \'%s\'' %(table_name, player_name))


		if(player_exist != ZERO):
			print("Player is Already in the Table.")
			raise()
			
		else:
			table_name = 'nbasite_team'

			team_exist = cursor.execute('SELECT * from %s where team_name = \'%s\'' %(table_name, team_name))


			if(team_exist == ZERO):
				print("Not Found Team.")
				#先创建新的队伍
				team_city = ''
				cursor.execute('INSERT into nbasite_team(`team_name`, `team_city`) values(\'%s\', \'%s\')' %(team_name, team_city))

				#再创建新的队员
				begin_date_str = begin_date.strftime("%Y-%m-%d")

				cursor.execute('INSERT into nbasite_player(`player_name`, `begin_date`, `team_id`) values(\'%s\', \'%s\', \'%s\')'
					%(player_name, begin_date_str, team_name))

			else:
				print("Found Team.")
				#直接创建队员
				begin_date_str = begin_date.strftime("%Y-%m-%d")
				cursor.execute('INSERT into nbasite_player(`player_name`, `begin_date`, `team_id`) values(\'%s\', \'%s\', \'%s\')'
					%(player_name, begin_date_str, team_name))

			return HttpResponse("Player %s has been added into %s." %(player_name, team_name))

	except:
		return HttpResponse("Player %s is already in the Table." %player_name)

def change_team_by_name(request, player_name, team_name):
	try:
		db_name = 'nba_database'
		conn.select_db(db_name)

		table_name = 'nbasite_player'

		number = cursor.execute("SELECT * from %s where player_name = \'%s\'" %(table_name, player_name))


		if(number == ZERO):
			print("Player is Not in the Table.")
			return HttpResponse("Change Fail. Player %s is Not in the Table!" % player_name)

		table_name = 'nbasite_team'
		team_exist = cursor.execute("SELECT * from %s where team_name = \'%s\'" %(table_name, team_name))

		if(team_exist == ZERO):
			team_city = ''
			cursor.execute('INSERT into nbasite_team(`team_name`, `team_city`) values(\'%s\', \'%s\')' %(team_name, team_city))
			print("Team Add Succeed.")

		table_name = 'nbasite_player'
		cursor.execute("UPDATE %s set `team_id` = \'%s\' where `player_name` = \'%s\'" %(table_name, team_name, player_name))

		return HttpResponse('Change %s\'s team succeed.' % player_name)

	except:
		return HttpResponse("Change Fail. Player %s is Not in the Table!" % player_name)




# def search_by_name(request, player_name):
# 	try:
# 		player = Player.objects.get(player_name = player_name)
# 		# content = request.POST.get('name')
# 		return HttpResponse("Team:" + str(player.team) + " Begin Date:" + str(player.begin_date))
# 	except Player.DoesNotExist:
# 		return HttpResponse("Player %s is Not in the Table!" % player_name)
# 	# return HttpResponse(player)

# def delete_by_name(request, player_name):
# 	try:
# 		old_player = Player.objects.get(player_name = player_name)
# 		old_player.delete()
# 		# return HttpResponse("Delete Succeed.")
# 		return HttpResponse("Player %s has been deleted successfully." % player_name)
# 	except Player.DoesNotExist:
# 		return HttpResponse("Player %s is Not in the Table!" % player_name)

# def change_team_by_name(request, player_name, team_name):
# 	try:
# 		player = Player.objects.get(player_name = player_name)
# 		try:
# 			new_team = Team.objects.get(team_name = team_name)
# 		except Team.DoesNotExist:
# 			new_team = Team(team_name = team_name)
# 			new_team.save()

# 		player.team = new_team
# 		player.save()
# 		return HttpResponse('Change %s\'s team succeed.' % player_name)
# 	except Player.DoesNotExist:
# 		return HttpResponse("Change Fail. Player %s is Not in the Table!" % player_name)

# def add_player(request, player_name, begin_date = datetime.datetime.now(), team_name = ''):

# 	try:
# 		old_player = Player.objects.get(player_name = player_name)
# 		return HttpResponse("Player %s is already in the Table." %player_name)
# 	except Player.DoesNotExist:
# 		try:
# 			team = Team.objects.get(team_name = team_name)
# 		except Team.DoesNotExist:
# 			team = Team(team_name = team_name)
# 			team.save()
# 			new_player = Player(player_name = player_name, begin_date = begin_date, team = team)
# 			new_player.save()
# 			return HttpResponse("Player %s has been added into %s." %(player_name, team_name))
# 			# return HttpResponse("TeamNotFound")

# 	new_player = Player(player_name = player_name, begin_date = begin_date, team = team)
# 	new_player.save()
# 	return HttpResponse("Player %s has been added into %s." %(player_name, team_name))
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