
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'owner']
        read_only_fields = ['id', 'created_at', 'owner']
