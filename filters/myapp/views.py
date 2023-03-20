# Create your views here.
from django.shortcuts import render
from .serializers import studentSerializer
from rest_framework.generics import ListAPIView
from .models import student
# Create your views here.
class studentList(ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    def get_queryset(self):
        user = self.request.user
        return student.objects.filter(passby=user)