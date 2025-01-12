from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AssistantViewSet, CommentViewSet

router = DefaultRouter()
router.register('assistants',AssistantViewSet, basename='assistants')
router.register('comment',CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]