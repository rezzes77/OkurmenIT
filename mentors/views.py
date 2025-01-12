from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MentorSerializers, MentorSessionSerializers
from .models import Mentor, MentorSession

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializers

class MentorSessionViewSet(viewsets.ModelViewSet):
    queryset = MentorSession.objects.all()
    serializer_class = MentorSessionSerializers