from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from storylabapi.models import Consequence



class ConsequenceView(ViewSet):

    def retrieve(self, request, pk):
        consequence = Consequence.objects.get(pk=pk)
        serializer = ConsequenceSerializer(consequence)
        return Response(serializer.data)
        
    def list(self, request):

        consequence = Consequence.objects.all()
        serializer = ConsequenceSerializer(consequence, many=True)
        return Response(serializer.data)
    
class ConsequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consequence
        fields = ('id', 'negResult')