"""View module for handling requests about seeds"""
from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Seed, Genre, Character, Desire, Fear, Obstacle, Consequence, Reward, Writer, Outline



class OutlineView(ViewSet):
    
    """Handle GET requests for single seed 
    Returns:
        Response -- JSON serialized seed
    """
    def retrieve(self, request, pk):
        outline = Outline.objects.get(pk=pk)
        serializer = OutlineSerializer(outline)
        return Response(serializer.data)
        


    def list(self, request):
        """
        Handle GET requests to get all seeds for the currently logged-in writer
        Returns:
            Response -- JSON serialized list of seeds
        """
        writer = Writer.objects.get(user=request.user)  # Retrieve the Writer object for the logged-in user
        outlines = Outline.objects.filter(writer=writer)  # Filter Outlines based on the writer
        serializer = OutlineSerializer(outlines, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized outline instance
        """
        writer = Writer.objects.get(user=request.auth.user)

        outline = Outline.objects.create(
            writer=writer,
            title=request.data["title"],
            prose=request.data["prose"]
        )

        serializer = OutlineSerializer(outline)
        return Response(serializer.data)
    

    def destroy(self, request, pk):
        outline = Outline.objects.get(pk=pk)
        outline.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


    
class OutlineSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Outline
        fields = ('id', 'writer', 'title', 'prose')
        depth = 2

    