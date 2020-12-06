from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Chat, Message
from .serializers import ChatSerializer


class ChatViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Chat.objects.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        chat = get_object_or_404(Chat, pk=pk)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        chat = get_object_or_404(Chat, pk=pk)
        chat.delete()
        return Response(status=status.HTTP_200_OK)
