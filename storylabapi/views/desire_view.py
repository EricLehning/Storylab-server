from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Desire



class DesireView(ViewSet):

    def retrieve(self, request, pk):
        desire = Desire.objects.get(pk=pk)
        serializer = DesireSerializer(desire)
        return Response(serializer.data)
        
    def list(self, request):

        desire = Desire.objects.all()
        serializer = DesireSerializer(desire, many=True)
        return Response(serializer.data)
    
class DesireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desire
        fields = ('id', 'wish')