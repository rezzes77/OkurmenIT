from rest_framework import serializers
from .models import Mentor, MentorSession

class MentorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class MentorSessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = MentorSession
        fields = '__all__'

