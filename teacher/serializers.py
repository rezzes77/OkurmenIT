from rest_framework import serializers
from .models import TeacherIT, TeacherENG, Exam, ExamResult, DailyScore, Homework

class TeacherITSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherIT
        fields = '__all__'

class TeacherEngSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherENG
        fields = '__all__'

class ExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ExamResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'

class DailyScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = DailyScore
        fields = '__all__'

class HomeworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

