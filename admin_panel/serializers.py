from rest_framework import serializers
from .models import Group, DaysOfWeek,Certificate, TaskAssistant

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysOfWeek
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class TaskAsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssistant
        fields = '__all__'

