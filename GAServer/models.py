from django.db import models

import json

class User(models.Model):

    id = models.IntegerField(primary_key=True)
    username = models.TextField()
    streak = models.IntegerField()

    def __str__(self):
        return str(self.username)

    def getJson(self):
        out = '{'
        out += f'"id" : {self.id},'
        out += f'"username" : "{self.username}",'
        out += f'"streak" : "{self.streak}"'
        out += '}'
        return out

class Level(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.TextField()
    description = models.TextField()

    def getJson(self):
        out = '{'
        out += f'"id" : {str(self.id)},' 
        out += f'"name" : "{str(self.name)}",'
        out += f'"description" : "{str(self.description)},"'
        out += '}'
        
        return out
    
class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.TextField()
    level = models.ForeignKey(Level, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.question)

    def getJson(self):
        out = '{'
        out += f'"id" : {str(self.id)},' 
        out += f'"question" : {str(self.question)},'
        out += f'"level" : {self.level.getJson()}'
        out += '}'
        return out


class Answer(models.Model):
    id = models.IntegerField(primary_key = True)
    content = models.TextField()
    isCorrect = models.BooleanField()
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def getJson(self):
        out = '{'
        out += f'"id" : {str(self.id)},' 
        out += f'"question" : "{str(self.question)}",'
        out += f'"content" : "{str(self.content)}",'
        out += f'"isCorrect" : "{str(self.isCorrect)}"'
        out += '}'

        return out

class Tutorial(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return str(self.username)


