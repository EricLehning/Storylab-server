from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Character



class CharacterView(ViewSet):

    def retrieve(self, request, pk):
        character = Character.objects.get(pk=pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
        
    def list(self, request):

        character = Character.objects.all()
        serializer = CharacterSerializer(character, many=True)
        return Response(serializer.data)
    
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'description')