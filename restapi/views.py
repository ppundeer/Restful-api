from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import superstore
from .serializers import storeSerializer

class storeList(APIView):
    def get(self, request):
        item = superstore.objects.all()[:20]
        serializer = storeSerializer(item, many=True)
        return Response(serializer.data)

    def post(self):
        pass
