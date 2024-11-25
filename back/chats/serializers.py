from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'user', 'user_message', 'ai_response', 'created_at']
        read_only_fields = ['ai_response', 'created_at']

    # def create(self, validated_data):
    #     from .utils import get_ai_response

    #     user_message = validated_data['user_message']
    #     ai_response = get_ai_response(user_message)
    #     validated_data['ai_response'] = ai_response
    #     return super().create(validated_data)