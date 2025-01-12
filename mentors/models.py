from django.db import models
from students.models import Student
from admin_panel.models import Group

class Mentor(models.Model):
    photo = models.ImageField(upload_to='mentor-img/', verbose_name='Фото ментора', blank=True, null=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон')
    specialization = models.CharField(
        max_length=100,
        choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Data Science', 'Data Science')],
        verbose_name='Специализация'
    )
    groups = models.ManyToManyField(Group, verbose_name='Группы', blank=True)
    bio = models.TextField(verbose_name='О менторе', blank=True)
    experience = models.IntegerField(verbose_name='Опыт работы (лет)', default=0)
    joined_date = models.DateField(verbose_name='Дата начала работы')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.specialization})'

class MentorSession(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, verbose_name='Ментор')
    students = models.ManyToManyField(Student, verbose_name='Студенты')
    date = models.DateTimeField(verbose_name='Дата сессии')
    duration = models.DurationField(verbose_name='Продолжительность')
    topic = models.CharField(max_length=200, verbose_name='Тема сессии')
    notes = models.TextField(verbose_name='Заметки ментора', blank=True)

    def __str__(self):
        return f'Сессия с {self.mentor.first_name} {self.mentor.last_name} ({self.date.strftime("%Y-%m-%d %H:%M")})'
