from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from statistics.models import Messages
from sets import Set

import json

# Create your views here.
def index(request):
	messages_manager = Messages.objects
	print messages_manager
	distinct_cities = Set([x.city for x in messages_manager.all()])
	distinct_users = Set([x.username for x in messages_manager.all()])
		
	return HttpResponse(json.dumps({
		'result':'success',
		'cities': len(distinct_cities),
		'users': len(distinct_users)
		}))