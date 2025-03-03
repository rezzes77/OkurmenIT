from django.db import models
# from admin_panel.models import Group
# from teacher.models import TeacherIT, TeacherENG
# from student.models import Student

class Assistant(models.Model):
    photo = models.ImageField(upload_to='assistant-img/', verbose_name='Фото ассистента')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    responsibilities = models.TextField(verbose_name='Список обязанностей')
    groups = models.ManyToManyField('admin_panel.Group', verbose_name='Группы', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} (Assistant)'

class Comment(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE,blank=True, null=True, verbose_name='Студент')
    teacherIT = models.ForeignKey('teacher.TeacherIT',on_delete=models.CASCADE,blank=True, null=True, verbose_name='Учитель по айти')
    teacherENG = models.ForeignKey('teacher.TeacherENG',on_delete=models.CASCADE,blank=True, null=True, verbose_name='Учитель по англ')
    text = models.TextField(verbose_name='Какое замечание')

