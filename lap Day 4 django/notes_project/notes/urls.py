from rest_framework import routers
from .views import NoteViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]
