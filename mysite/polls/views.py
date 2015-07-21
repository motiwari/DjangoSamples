from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from polls.models import Question, Choice
from sets import Set

import json

# Create your views here.
def index(request):
	Q = Question.objects
	Stringoutput  = ""
	Questionsyo = Set(map(str,Q.all()))
		
	return HttpResponse(json.dumps({'1': map(str,Questionsyo)}))