# Generated by Django 5.1.4 on 2025-01-12 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0001_initial'),
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Какое замечание')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Студент')),
                ('teacherENG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teachereng', verbose_name='Учитель по англ')),
                ('teacherIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacherit', verbose_name='Учитель по айти')),
            ],
        ),
    ]
