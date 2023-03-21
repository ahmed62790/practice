from django.shortcuts import render

# Create your views here.
from .models import student
from .serializers import studentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class studentModelViewSet(viewsets.ModelViewSet):
    
    queryset = student.objects.all ()
    serializer_class = studentSerializer
  #  authentication_classes = [BasicAuthentication] 
 #   permission_classes = [IsAuthenticated]
  #  permission_classes = [IsAdminUser]
