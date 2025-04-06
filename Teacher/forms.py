from . models import Exam,MarkingScheme,AnswerSheets

from django import forms

class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields=['examname','examabout']

class MarkingSchemeForm(forms.ModelForm):
    class Meta:
        model=MarkingScheme
        fields=['markingschemepic']

class AnswerSheetForm(forms.ModelForm):
    class Meta:
        model=AnswerSheets
        fields=['answersheetpic','studentname','studentroll']