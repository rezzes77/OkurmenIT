from django.shortcuts import render
from rest_framework import viewsets
from .serializers import  StudentSerializers
from .models import  Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

