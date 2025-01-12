# Generated by Django 5.1.4 on 2025-01-12 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0002_comment'),
        ('student', '0001_initial'),
        ('teacher', '0002_dailyscore_exam_examresult_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='teacherENG',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teachereng', verbose_name='Учитель по англ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='teacherIT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacherit', verbose_name='Учитель по айти'),
        ),
    ]
