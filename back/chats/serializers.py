# chats/serializers.py

from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'user', 'user_message', 'ai_response', 'created_at']
        read_only_fields = ['ai_response', 'created_at']