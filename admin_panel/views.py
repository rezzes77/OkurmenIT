from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GroupSerializer, DaysSerializer, CertificateSerializer, TaskAsSerializer
from .models import Group, DaysOfWeek, Certificate, TaskAssistant

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DaysViewSet(viewsets.ModelViewSet):
    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskAssistant.objects.all()
    serializer_class = TaskAsSerializer
