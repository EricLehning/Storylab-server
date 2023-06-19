from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Writer



class WriterView(ViewSet):

    def retrieve(self, request, pk):
        writer = Writer.objects.get(pk=pk)
        serializer = WriterSerializer(writer)
        return Response(serializer.data)
        
    def list(self, request):

        writer = Writer.objects.get(user=request.user)
        serializer = WriterSerializer(writer)
        return Response(serializer.data)
    
class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ('id', 'user', 'penName', 'profilePic')