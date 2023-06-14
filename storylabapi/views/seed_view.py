"""View module for handling requests about seeds"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from storylabapi.models import Seed


class SeedView(ViewSet):
    """Story Lab Seed view"""
    """Handle GET requests for single seed 
    Returns:
        Response -- JSON serialized seed
    """
    def retrieve(self, request, pk):
        seed = Seed.objects.get(pk=pk)
        serializer = SeedSerializer(seed)
        return Response(serializer.data)
        


    def list(self, request):
        """Handle GET requests to get all seeds
        Returns:
            Response -- JSON serialized list of seeds
        """
        seeds = Seed.objects.all()
        serializer = SeedSerializer(seeds, many=True)
        return Response(serializer.data)
    
class SeedSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Seed
        fields = ('id', 'user', 'title', 'genre', 'character', 'desire', 'fear', 'obstacles', 'consequence', 'reward')
