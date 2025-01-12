# from django.contrib import admin
# from teacher.models import DailyScore
# from student.models import Student
# from .models import Group
# from teacher.models import TeacherIT, TeacherENG
#
#
# @admin.register(DailyScore)
# class DailyScoreAdmin(admin.ModelAdmin):
#     list_display = ('student', 'date', 'score')
#     list_filter = ('date', 'student__group')
#     search_fields = ('student__first_name', 'student__last_name', 'student__group__name')
#
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('photo_preview', 'last_name', 'first_name', 'group', 'total_score')
#     search_fields = ('first_name', 'last_name', 'group__name')
#     list_filter = ('group',)
#
#     def photo_preview(self, obj):
#         if obj.photo:
#             return f'<img src="{obj.photo.url}" style="height: 50px; width: 50px; object-fit: cover;" />'
#         return "Нет фото"
#     photo_preview.short_description = 'Фото'
#     photo_preview.allow_tags = True
#
#     def total_score(self, obj):
#         from teacher.models import DailyScore
#         total = DailyScore.objects.filter(student=obj).aggregate(total=models.Sum('score'))['total']
#         return total if total else 0
#     total_score.short_description = 'Общий балл'
#
#
#
#
# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('name', 'student_count', 'list_students')
#     search_fields = ('name',)
#
#     def student_count(self, obj):
#         return obj.student_set.count()
#
#     student_count.short_description = 'Количество учеников'
#
#     def list_students(self, obj):
#         students = obj.student_set.all()
#         return ', '.join([f"{student.first_name} {student.last_name}" for student in students])
#
#     list_students.short_description = 'Ученики'
#
# @admin.register(TeacherIT)
# class TeacherITAdmin(admin.ModelAdmin):
#     list_display = ('photo_preview', 'name', 'group_count', 'student_count')
#     search_fields = ('name',)
#
#     def photo_preview(self, obj):
#         if obj.photo:
#             return f'<img src="{obj.photo.url}" style="height: 50px; width: 50px; object-fit: cover;" />'
#         return "Нет фото"
#     photo_preview.short_description = 'Фото'
#     photo_preview.allow_tags = True
#
#     def group_count(self, obj):
#         return obj.group_set.count()
#     group_count.short_description = 'Количество групп'
#
#     def student_count(self, obj):
#         return sum(group.student_set.count() for group in obj.group_set.all())
#     student_count.short_description = 'Количество учеников'
#
# @admin.register(TeacherENG)
# class TeacherENGAdmin(TeacherITAdmin):
#     pass
