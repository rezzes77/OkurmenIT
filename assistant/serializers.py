from rest_framework import serializers
from .models import Assistant, Comment

class AssistantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

