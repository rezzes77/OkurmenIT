from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

router = DefaultRouter()
router.register('students',StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls))
]