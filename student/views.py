from django.shortcuts import render
from rest_framework import viewsets
from .serializers import  StudentSerializers
from .models import  Student
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from teacher.models import Homework, Exam
from student.models import Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers



@login_required
def notifications_view(request):
    student = Student.objects.get(email=request.user.email)

    homeworks = Homework.objects.filter(group=student.group)
    exams = Exam.objects.filter(group=student.group)

    data = {
        "homeworks": [
            {
                "id": hw.id,
                "group": hw.group.name,
                "homework": hw.homework,
            }
            for hw in homeworks
        ],
        "exams": [
            {
                "id": exam.id,
                "group": exam.group.name,
                "date": exam.date,
                "where": exam.where,
                "url": exam.url if exam.url else None,
            }
            for exam in exams
        ],
    }

    return JsonResponse(data)
