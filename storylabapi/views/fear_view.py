from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Fear



class FearView(ViewSet):

    def retrieve(self, request, pk):
        fear = Fear.objects.get(pk=pk)
        serializer = FearSerializer(fear)
        return Response(serializer.data)
        
    def list(self, request):

        fear = Fear.objects.all()
        serializer = FearSerializer(fear, many=True)
        return Response(serializer.data)
    
class FearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fear
        fields = ('id', 'fearName')