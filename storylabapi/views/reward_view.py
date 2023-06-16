from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Reward



class RewardView(ViewSet):

    def retrieve(self, request, pk):
        reward = Reward.objects.get(pk=pk)
        serializer = RewardSerializer(reward)
        return Response(serializer.data)
        
    def list(self, request):

        reward = Reward.objects.all()
        serializer = RewardSerializer(reward, many=True)
        return Response(serializer.data)
    
class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('id', 'prize')