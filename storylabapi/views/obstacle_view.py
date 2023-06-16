from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Obstacle



class ObstacleView(ViewSet):

    def retrieve(self, request, pk):
        obstacle = Obstacle.objects.get(pk=pk)
        serializer = ObstacleSerializer(obstacle)
        return Response(serializer.data)
        
    def list(self, request):

        obstacle = Obstacle.objects.all()
        serializer = ObstacleSerializer(obstacle, many=True)
        return Response(serializer.data)
    
class ObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacle
        fields = ('id', 'obstruction')