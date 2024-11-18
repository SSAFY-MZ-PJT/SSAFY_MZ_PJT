from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ReviewListSerializer, ReviewSerializer
from .models import Review


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewListSerializer(reviews, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)