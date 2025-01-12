from django.shortcuts import render
from rest_framework import viewsets
from .serializers import  TeacherITSerializers, TeacherEngSerializers, ExamSerializers, ExamResultSerializers, DailyScoreSerializers, HomeworkSerializers
from .models import TeacherIT, TeacherENG, Exam, ExamResult, DailyScore, Homework

class TeacherITViewSet(viewsets.ModelViewSet):
    queryset = TeacherIT.objects.all()
    serializer_class = TeacherITSerializers

class TeacherEngViewSet(viewsets.ModelViewSet):
    queryset = TeacherENG.objects.all()
    serializer_class = TeacherEngSerializers

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers

class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializers

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers

class DailyScoreViewSet(viewsets.ModelViewSet):
    queryset = DailyScore.objects.all()
    serializer_class = DailyScoreSerializers