from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, DaysViewSet, CertificateViewSet, TaskViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet, basename='groups')
router.register('days',DaysViewSet, basename='days')
router.register('certificate', CertificateViewSet, basename='certificate')
router.register('task for assistant',TaskViewSet, basename='task for assistant')

urlpatterns = [
    path('', include(router.urls))
]