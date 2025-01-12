from django.db import models
from teacher.models import TeacherIT,TeacherENG
from admin_panel.models import Group

class Student(models.Model):
    photo = models.ImageField(upload_to='student-img/', verbose_name='Фото студента')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    specialization = models.CharField(max_length=50, choices=[('Frontend', 'Frontend'), ('Backend', 'Backend')], verbose_name='Направление')
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='Возраст')
    teacher_it = models.ManyToManyField(TeacherIT, verbose_name='Учитель по айти')
    teacher_eng = models.ManyToManyField(TeacherENG, verbose_name='Учитель по английскому')
    joined_date = models.DateField(verbose_name='Дата начала обучения')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.specialization})'

