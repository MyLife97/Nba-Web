from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Player, Team
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
# Create your views here.

def home(request):

	return render(request, 'NbaSite/home.html')