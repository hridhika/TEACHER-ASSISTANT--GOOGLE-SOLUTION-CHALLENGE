from django.contrib import admin
from . models import Exam,MarkingScheme,AnswerSheets,Results
# Register your models here.

admin.site.register(Exam)
admin.site.register(MarkingScheme)
admin.site.register(AnswerSheets)
admin.site.register(Results)


