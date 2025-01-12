from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeacherITViewSet, TeacherEngViewSet, ExamViewSet, ExamResultViewSet, DailyScoreViewSet, HomeworkViewSet

router = DefaultRouter()
router.register('teacherIT',TeacherITViewSet, basename='teacherIT')
router.register('teacherENG',TeacherEngViewSet, basename='teacherENG')
router.register('exam',ExamViewSet, basename='exam')
router.register('exam-result',ExamResultViewSet, basename='exam-result')
router.register('score',DailyScoreViewSet, basename='score')
router.register('homework',HomeworkViewSet, basename='homework')


urlpatterns = [
    path('', include(router.urls))
]