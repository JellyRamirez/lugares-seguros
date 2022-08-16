from os import stat
from re import A
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Comments 
from .serializers import CommentsSerializer, CommentPlaceListSerializer


class CommentView(APIView):

    def get(self, request):

        comment= Comments.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CommentOnlyView(APIView):
    def patch(self, request, pk):
        comment = Comments.objects.filter(pk=pk).first()

        if comment is None:
            return Response({'error':'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CommentsSerializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        comment = get_object_or_404(Comments, pk=pk)
        comment.delete()
        return Response('Comentario eliminado', status=status.HTTP_204_NO_CONTENT)
