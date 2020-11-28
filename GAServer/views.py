from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json

from GAServer.models import Question, User

# Create your views here
# --Get Request--

def users(request, userID = -1):
    u = User(id = 0, username = "Eric")
    u.save()

    if userID < 0:
        print("Huhu")
        allUsers = User.objects.all()

        jsonObjects = [] 
        jsonObjects += allUsers

        
        print()

    else:
        pass

    return HttpResponse(Question.arrayToJson(jsonObjects), content_type = "application/json")