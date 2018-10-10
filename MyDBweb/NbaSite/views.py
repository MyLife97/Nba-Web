from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404, JsonResponse
from .models import Player, Team
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

import json
# Create your views here.



def home(request):
	return render(request, 'NbaSite/home.html')

def search_by_name(request, player):
	try:
		player_name = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})


	return HttpResponse(player)

# def ajax_test(request):
# 	name = 'James'
# 	return JsonResponse(name, safe = False)	

# def ajax_test(request):
#     user_name = request.POST.get("username")
#     password = request.POST.get("password")
#     print(user_name, password)
#     # i += 1
#     return HttpResponse("i")