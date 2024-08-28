from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class PostTest(APIView):
    def get(self, request):
        return Response({"success": True, "message": "OK"}, status=200)