from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MentorViewSet, MentorSessionViewSet

router = DefaultRouter()
router.register('mentors',MentorViewSet, basename='mentors')
router.register('mentor-session',MentorSessionViewSet, basename='mentor-session')

urlpatterns = [
    path('', include(router.urls))
]