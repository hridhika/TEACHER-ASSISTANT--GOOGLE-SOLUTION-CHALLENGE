from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('teacherhome/',views.TeacherHome,name="teacherhome"),
    path('examcreate/',views.ExamCreate,name='examcreate'),
    path('markingschemecreate/<id>',views.MarkingSchemeCreate,name='markingschemecreate'),
    path('singlemarkingschemeview/<id>',views.SingleMarkingSchemeView,name='singlemarkingschemeview'),
    path('answersheetcreate/<id>',views.AnswerSheetCreate,name='answersheetcreate'),
    path('answersheetview/<id>',views.AnswerSheetsView,name='answersheetview'),
    path('results/<id>',views.EvaluateExam,name='evaluateexam'),
]