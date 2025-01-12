from django.db import models
from student.models import Student
from assistant.models import Assistant

class DaysOfWeek(models.Model):
    name = models.CharField(max_length=20, verbose_name='День недели', unique=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя группы', unique=True)
    time_start = models.TimeField(verbose_name='Начало урока')
    time_end = models.TimeField(verbose_name='Конец урока')
    work_days = models.ManyToManyField(DaysOfWeek, verbose_name='Дни занятий')
    month = models.IntegerField(verbose_name='Месяц')

    def __str__(self):
        return f'{self.name} : {self.time_start}-{self.time_end}, месяц: {self.month}'

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=[('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze')])
    total_points = models.IntegerField()
    date_issued = models.DateField()

    def __str__(self):
        return f'{self.student.name} - {self.level} Certificate'

class TaskAssistant(models.Model):
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, verbose_name='Ассистент')
    date = models.DateField(verbose_name='На какую дату')
    tasks = models.TextField(verbose_name='Список задач')

