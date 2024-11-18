from rest_framework import serializers
from .models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('pk', 'title', 'content', 'user')

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)