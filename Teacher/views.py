from django.shortcuts import render,redirect
from . forms import ExamForm,MarkingSchemeForm,AnswerSheetForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . models import Exam,MarkingScheme,AnswerSheets,Results
import os
from django.core.files import File
from django.conf import settings
# Create your views here.

@login_required(login_url=reverse_lazy('auth'))
def TeacherHome(request):
    role=request.user.usertype.usertype
    if(role=='teacher'):
        exams=Exam.objects.filter(owner=request.user)
    else:
        exams=Exam.objects.all()
    return render(request,"teacherhome.html",{'exams':exams,'role':role})

@login_required(login_url=reverse_lazy('auth'))
def ExamCreate(request):
    if request.POST:
        frm=ExamForm(request.POST)
        if frm.is_valid():
            exam=frm.save(commit=False)
            exam.owner=request.user
            exam.save()
            return redirect('teacherhome')
    frm=ExamForm()
    return render(request,'examform.html',{'frm':frm})

@login_required(login_url=reverse_lazy('auth'))
def MarkingSchemeCreate(request,id):
    if request.POST:
        frm = MarkingSchemeForm(request.POST, request.FILES)
        if frm.is_valid():
            markingscheme=frm.save(commit=False)
            exam=Exam.objects.get(id=id)
            markingscheme.owner=exam
            markingscheme.save()
            return redirect('teacherhome')
    frm=MarkingSchemeForm()
    return render(request,"markingschemeform.html",{'frm':frm})

def SingleMarkingSchemeView(request,id):
    exam=Exam.objects.get(id=id)
    mscheme=MarkingScheme.objects.get(owner=exam)
    return render(request,"singlemarkingscheme.html",{'mscheme':mscheme})

def AnswerSheetCreate(request,id):
    if request.POST:
        frm = AnswerSheetForm(request.POST, request.FILES)
        if frm.is_valid():
            answersheet=frm.save(commit=False)

            exam=Exam.objects.get(id=id)
            answersheet.ownerexam=exam

            mscheme=MarkingScheme.objects.get(owner=exam)
            answersheet.ownermarkingscheme=mscheme

            answersheet.save()
            return redirect('teacherhome')
    frm=AnswerSheetForm()
    return render(request,"answersheetform.html",{'frm':frm})

def AnswerSheetsView(request,id):
    exam=Exam.objects.get(id=id)
    answersheets=AnswerSheets.objects.filter(ownerexam=exam)
    return render(request,"viewanswersheets.html",{'answersheets':answersheets})


import re
from PIL import Image
import google.generativeai as genai
from django.shortcuts import render, get_object_or_404
from .models import Exam, MarkingScheme, AnswerSheets

# Configure Gemini API
genai.configure(api_key="AIzaSyCtSoakhqLnf9mXGkVSTZ6dX3YgjflImIc") 
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def parse_teacher_text(text):
    pattern = r"(Q\d+):\s*(.+?)\s*\((\d+)\)"
    return {
        qid: {"answer": ans.strip(), "marks": int(marks)}
        for qid, ans, marks in re.findall(pattern, text, re.DOTALL)
    }

def parse_student_text(text):
    pattern = r"(Q\d+):\s*(.+?)(?=\nQ\d+:|\Z)"
    return dict(re.findall(pattern, text, re.DOTALL))

def EvaluateExam(request, id):
    exam = get_object_or_404(Exam, id=id)
    mscheme = get_object_or_404(MarkingScheme, owner=exam)

    if Results.objects.filter(exam=exam).exists():

        results = Results.objects.filter(exam=exam)

        result_data = []

        for r in results:
            try:
                with r.result.open('r') as f:
                    content = f.read()
            except Exception as e:
                content = f"⚠️ Could not read file: {e}"

            print(content)

            result_data.append({
                "studentname": r.owner.studentname,
                "studentroll": r.owner.studentroll,
                "file_url": r.result.url,
                "content": content
            })

        print(result_data)

        return render(request, "test.html", {"result_data": result_data})


    teacher_image = Image.open(mscheme.markingschemepic.path)
    extract_prompt = """Extract all the text from this image exactly as written, including question numbers and marks in brackets if present. Keep the format as it appears (e.g., Q1: ... (3)). Return only the text, no extra commentary."""
    
    teacher_response = model.generate_content([extract_prompt, teacher_image])
    teacher_raw_text = teacher_response.text.strip()
    teacher_answers = parse_teacher_text(teacher_raw_text)

    results = []

    answersheets = AnswerSheets.objects.filter(ownerexam=exam)
    for sheet in answersheets:
        student_data = {
            "name": sheet.studentname,
            "roll": sheet.studentroll,
            "score": 0,
            "evaluations": []  
        }

        student_image = Image.open(sheet.answersheetpic.path)
        student_response = model.generate_content([extract_prompt, student_image])
        student_raw_text = student_response.text.strip()
        student_answers = parse_student_text(student_raw_text)

        total_score = 0
        for qid, student_ans in student_answers.items():
            if qid in teacher_answers:
                teacher_ans = teacher_answers[qid]["answer"]
                max_marks = teacher_answers[qid]["marks"]

                grade_prompt = f"""
You're an exam evaluator. Grade the following student's answer to a question.
Be slightly lenient for spelling mistakes or wording, but ensure the main idea and concepts are present.

Answer Key:
{teacher_ans}

Student Answer:
{student_ans}

Give only the marks out of {max_marks} and a short one-line justification.
"""
                grading_response = model.generate_content(grade_prompt).text.strip()


                match = re.search(r"(\d+(\.\d+)?)\s*/?\s*" + str(max_marks), grading_response)
                marks_awarded = float(match.group(1)) if match else 0

                total_score += marks_awarded

                student_data["evaluations"].append({
                    "question": qid,
                    "feedback": grading_response,
                    "awarded": marks_awarded,
                    "out_of": max_marks
                })
            else:
                student_data["evaluations"].append({
                    "question": qid,
                    "feedback": "❌ No matching question in teacher answers.",
                    "awarded": 0,
                    "out_of": 0
                })

        student_data["score"] = total_score
        results.append(student_data)

        txt_content = f"Name: {sheet.studentname}\nRoll: {sheet.studentroll}\nTotal Score: {student_data['score']}\n\n"
        for eval in student_data["evaluations"]:
            txt_content += f"{eval['question']}: {eval['feedback']} ({eval['awarded']}/{eval['out_of']})\n"
        
        results_dir = os.path.join(settings.MEDIA_ROOT, "results")
        os.makedirs(results_dir, exist_ok=True)

        filename = f"{sheet.studentroll}_result.txt"
        file_path = os.path.join(results_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(txt_content)

        with open(file_path, "rb") as f:
            django_file = File(f)
            result_obj, created = Results.objects.get_or_create(owner=sheet,exam=exam)

            result_obj.result.save(filename, django_file, save=True)

    return render(request, "results.html", {"results": results})
