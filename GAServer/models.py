from django.db import models

import json

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.TextField()
    answers = [models.TextField()]
    

    def __init__(self,question, answers):
        self.question = question
        self.answers = answers

    def __str__(self):
        return str(self.question)

    def getJson(self):
        out = '{'
        out += f'"id" : {str(self.id)},' 
        out += f'"question" : {str(self.question)}'
        arr = str(self.answers).replace("'",'"')
        out += f'"answers" : {arr}' 
        out += '}'

        return out
    
    def arrayToJson(arr):
        out = '['

        for i in arr:
            out += i.getJson() + ","
        
        out = out[:-1]
        out += ']'
        return out

class User(models.Model):

    id = models.IntegerField(primary_key=True)
    username = models.TextField()

    def __str__(self):
        return str(self.username)

    def getJson(self):
        out = '{'
        out += f'"id" : {self.id},'
        out += f'"username" : "{self.username}"'
        out += '}'
        return out
