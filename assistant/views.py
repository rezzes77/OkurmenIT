from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AssistantSerializers, CommentSerializers
from .models import Assistant, Comment

class AssistantViewSet(viewsets.ModelViewSet):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializers

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers