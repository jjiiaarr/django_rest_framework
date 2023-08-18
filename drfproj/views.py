from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# from drfproj.drfapp.serializers import StudentSerializer

from .serializers import StudentsSerializer
from .models import Student


class TesView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'years_active': 10
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
