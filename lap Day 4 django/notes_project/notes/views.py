from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return notes belonging to the authenticated user
        return Note.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Assign the logged-in user as owner
        serializer.save(owner=self.request.user)
