from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json

from GAServer.models import *

# Create your views here
# -- Helper Functions --
def arrayToJson(arr):
    out = '['

    for i in arr:
        out += i.getJson() + ","
        
    out = out[:-1]
    out += ']'
    return out

def createUserFromJson(js):
    dict = json.loads(js)
    #count the current user in order to find the id
    users = User.objects.all()
    
    return User(
        id = len(users),
        username = dict["username"],
        streak = dict["streak"]
    )

def createAnswerFromJson(js):
    dict = json.loads(js)
    answers = Answer.objects.all()

    return Answer(
        id = len(answers),
        content = dict["content"],
        isCorrect = dict["isCorrect"],
        question = Question.objects.get(id = dict["questionid"])
    )
    

def createQuestionFromJson(js):
    dict = json.loads(js)
    allQuestions = Question.objects.all()

    return Question(
        id = len(allQuestions),
        question = dict["question"],
        level = Level.objects.get(id = dict["levelid"])
    )

# --Get Request--
def initDatabase(request):
    u = User(id = 0, username = "Eric", streak = 0)
    u.save()

    t = Tutorial(id = 0, title = "TestTutorial", instructions = "test instructions")
    t.save()

    l = Level(id = 0, name = "Level0", description = "This is a test level")
    l.save()

    q = Question(id = 0, question = "What is this?", level = Level.objects.get(id = 0))      
    q.save()

    a = Answer(id = 0, content = "Racing or ping pong", question = Question.objects.get(id = 0), isCorrect = True)
    a.save()
 
    return HttpResponse("ok")

def users(request, userID = -1):

    if userID < 0:
        print("Huhu")
        allUsers = User.objects.all()
        jsonObjects = []
        jsonObjects += allUsers


    else:
        pass

    return HttpResponse(arrayToJson(jsonObjects), content_type = "application/json")

def questions(request, levelid = -1):
    
    if levelid < 0:
        questions = Question.objects.all()
        res = arrayToJson(questions)
    else:
        question = Question.objects.get(id = levelid)
        res = question.toJson()

    return HttpResponse(res, content_type = "application/json")

def answers(request, answerid = -1):

    if answerid < 0:
        answers = Answer.objects.all()
        print(answers)
        res = arrayToJson(answers)
    else: 
        answer = Answer.objects.get(id = answerid)
        res = answer.toJson()

    return HttpResponse(res, content_type = "application/json")

def answersOfQuestion(request, questionid = -1):
    if questionid < 0:
        pass
    else: 
        answers = Answer.objects.filter(question_id = questionid)
        #print(answers[0].getJson())

    return HttpResponse(arrayToJson(answers), content_type = "application/json")

def incrementUserStreak(request, userid = -1):
    if userid < 0:
        return HttpResponse("400 Bad request")
    else:
        user = User.objects.get(id = userid)
        user.streak = user.streak + 1
        user.save()

        user = User.objects.get(id = userid)
    return HttpResponse(user.getJson(), content_type = "application/json")

# -- Post requests --
@require_http_methods(['POST'])
def createUser(request):
    requestBody = request.read().decode('utf-8')

    user = createUserFromJson(requestBody)
    user.save()
    print("added user: " + user.username)
    return HttpResponse("OK")

@require_http_methods(['POST'])
def setUser(request, userid = -1): 
    requestBody = request.read().decode('utf-8')

    if userid < 0:
        return HttpResponse("400 Bad request")
    else:
        user = User.objects.get(id = userid)
        user = createUserFromJson(requestBody)
        user.save()

@require_http_methods(['POST'])
def createQuestion(request):

    requestBody = request.read().decode('utf-8')

    question = createQuestionFromJson(requestBody)
    question.save()

    return HttpResponse("OK")

@require_http_methods(['POST'])
def createAnswer(request):
    requestBody = request.read().decode('utf-8')
    
    answer = createAnswerFromJson(requestBody)
    answer.save()

    return HttpResponse("OK")



@require_http_methods(['POST'])
def createLevel(request):
    requestBody = request.read().decode('utf-8')

    level = createLevelFromJson(requestBody)
    level.save()

    return HttpResponse("OK")

