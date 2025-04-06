from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exam(models.Model):
    examname=models.CharField(max_length=100)
    examabout=models.TextField(max_length=200,null=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='exams')

class MarkingScheme(models.Model):
    markingschemepic=models.ImageField(upload_to='markingschemes/')
    owner=models.OneToOneField(Exam,on_delete=models.CASCADE,related_name='markingscheme')

class AnswerSheets(models.Model):
    answersheetpic=models.ImageField(upload_to='answersheets/')
    studentname=models.CharField(max_length=50)
    studentroll=models.CharField(max_length=10)
    ownermarkingscheme=models.ForeignKey(MarkingScheme,on_delete=models.CASCADE,related_name='answersheet')
    ownerexam=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='answersheet')

class Results(models.Model):
    result=models.FileField(upload_to='results/')
    owner=models.OneToOneField(AnswerSheets,on_delete=models.CASCADE,related_name='results')
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='results',null=True)