from django.db import models
from admin_panel.models import Group, DaysOfWeek

class TeacherIT(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
    ]
    photo = models.ImageField(upload_to='teacher-img/', verbose_name='Фото учителя')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES, verbose_name='Направление')
    groups = models.ManyToManyField(Group, verbose_name='Группы')
    joined_date = models.DateField(verbose_name='Дата присоединения')
    work_days = models.ManyToManyField(DaysOfWeek, verbose_name='Дни работы')
    experience = models.CharField(max_length=50, verbose_name='Опыт работы')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.specialization})'

class TeacherENG(models.Model):
    photo = models.ImageField(upload_to='teacher-img/', verbose_name='Фото учителя')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    groups = models.ManyToManyField(Group, verbose_name='Группы')
    joined_date = models.DateField(verbose_name='Дата присоединения')
    work_days = models.ManyToManyField(DaysOfWeek, verbose_name='Дни работы')
    experience = models.CharField(max_length=50, verbose_name='Опыт работы')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name} (English)'

class Exam(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    date = models.DateField(verbose_name='Дата экзамена')
    where = models.CharField(max_length=50, verbose_name='Место провождение', choices=[
        ('Онлайн', 'Онлайн'),
        ('Оффлайн', 'Оффлайн'),
    ])
    url = models.URLField(verbose_name='Ссылка на экзамен(если онлайн)', blank=True, null=True)
    teacher = models.ForeignKey(TeacherIT, TeacherENG, verbose_name='Учитель')

class ExamResult(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    student = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Студент')
    teacher = models.ForeignKey(TeacherIT, TeacherENG, verbose_name='Учитель')
    result = models.CharField(max_length=50, verbose_name='Результат', choices=[
        ('Прошел', 'Прошел'),
        ('Провалил', 'Провалил'),
        ('Пересдача', 'Пересдача'),
    ])

class Homework(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    student = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Студент')
    homework = models.TextField(verbose_name='Домашнее задание')


class DailyScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.score} - {self.date}'


