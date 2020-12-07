"""name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path

from GAServer import views

class Test:
    def __init__():
        return "Test"

    def __str__():
        return "nothing"

    def test(args):
        return HttpResponse("test", content_type = "text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.users, name="users"),
    path('createUser/', views.createUser, name="createUser"),
    path('questions/', views.questions, name = "questions"),
    path('createQuestion/', views.createQuestion, name = "createQuestion"),
    path('answers/', views.answers, name = "answers"),
    path('createAnswer/', views.createAnswer, name = "createAnswer"),
    path('answersOfQuestion/<int:questionid>', views.answersOfQuestion, name = "answersOfQuestion"),
    path('incrementStreak/<int:userid>', views.incrementUserStreak, name="incrementUserStreak"),
    path('initDatabase/', views.initDatabase, name="initDatabase")

]




