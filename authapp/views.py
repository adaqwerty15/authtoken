from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework import permissions
import requests


class PasswordConfirmationView(APIView):
    def get (self, request, uid, token):
        return redirect('http://localhost:8081/#/setpass/{}/{}'.format(uid, token))

class GetInformation(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get (self, request):
        return Response({'information': 'it is closed information'})  

# Create your views here.
