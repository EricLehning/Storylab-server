"""View module for handling requests about seeds"""
from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Seed, Genre, Character, Desire, Fear, Obstacle, Consequence, Reward, Writer



class SeedView(ViewSet):
    
    """Handle GET requests for single seed 
    Returns:
        Response -- JSON serialized seed
    """
    def retrieve(self, request, pk):
        seed = Seed.objects.get(pk=pk)
        serializer = SeedSerializer(seed)
        return Response(serializer.data)
        


    def list(self, request):
        """
        Handle GET requests to get all seeds for the currently logged-in writer
        Returns:
            Response -- JSON serialized list of seeds
        """
        writer = Writer.objects.get(user=request.user)  # Retrieve the Writer object for the logged-in user
        seeds = Seed.objects.filter(writer=writer)  # Filter seeds based on the writer
        serializer = SeedSerializer(seeds, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized seed instance
        """
        writer = Writer.objects.get(user=request.auth.user)
        genre = Genre.objects.get(pk=request.data["genre"])
        character = Character.objects.get(pk=request.data["character"])
        desire = Desire.objects.get(pk=request.data["desire"])
        fear = Fear.objects.get(pk=request.data["fear"])
        obstacles = [Obstacle.objects.get(pk=obstacle_id) for obstacle_id in request.data.get("obstacles", [])]
        consequence = Consequence.objects.get(pk=request.data["consequence"])
        reward = Reward.objects.get(pk=request.data["reward"])

        seed = Seed.objects.create(
            writer=writer,
            title=request.data["title"],
            genre=genre,
            character=character,
            desire=desire,
            fear=fear,
            consequence=consequence,
            reward=reward
        )

        # Assign the obstacles to the seed's obstacle field
        seed.obstacles.set(obstacles)

        serializer = SeedSerializer(seed)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a seed

        Returns:
            Response -- Empty body with a 204 status code
        """

        seed = Seed.objects.get(pk=pk)
        genre = Genre.objects.get(pk=request.data["genre"])
        character = Character.objects.get(pk=request.data["character"])
        desire = Desire.objects.get(pk=request.data["desire"])
        fear = Fear.objects.get(pk=request.data["fear"])
        consequence = Consequence.objects.get(pk=request.data["consequence"])
        reward = Reward.objects.get(pk=request.data["reward"])
        
        seed.title = request.data["title"]
        seed.genre = genre
        seed.character = character
        seed.desire = desire
        seed.fear = fear
        seed.consequence = consequence
        seed.reward = reward

        #update obstacles to the seed's obstacle field
        obstacles = [Obstacle.objects.get(pk=obstacle_id) for obstacle_id in request.data.get("obstacles", [])]
        seed.obstacles.set(obstacles)
        seed.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        seed = Seed.objects.get(pk=pk)
        seed.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


    
class SeedSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Seed
        fields = ('id', 'writer', 'title', 'genre', 'character', 'desire', 'fear', 'obstacles', 'consequence', 'reward')
        depth = 2

    