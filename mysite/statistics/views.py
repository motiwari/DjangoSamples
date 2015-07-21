from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from statistics.models import Messages
from sets import Set
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

import json

# Create your views here.
def index(request):
	messages_manager = Messages.objects
	try:
		distinct_cities = Set([x.city for x in messages_manager.all()])
		distinct_users = Set([x.username for x in messages_manager.all()])
		
		#Uncomment this line to test handling
		#print distinct_users[4]

		response = HttpResponse(json.dumps({
			'result':'success',
			'cities': len(distinct_cities),
			'users': len(distinct_users)
			}))


	except Exception as e:
		logger.error('Something went wrong!')
		response = HttpResponse(json.dumps({
			'result':'error',
			'error' : str(e)
			}))
		pass

	#Delay in seconds
	response['refresh'] = 60
	return response

