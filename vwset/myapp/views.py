from django.shortcuts import render
from rest_framework.response import Response
from .models import student
from .serializers import studentSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.


class studentViewset(viewsets.ViewSet):
    def List(self, request):
        stu = student.objects.all()
        serializer = studentSerializer(stu, many = True)
        return Response(serializer.data)
    

    def retrieve(self,request, pk = None):
        id = pk
        if id is not None:
            stu = student.objects.get(id=id)
            serializer = studentSerializer(stu)
            return Response(serializer.data)
        
    def create(self, request):
        serializer = studentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id= pk
        stu = student.objects.get(pk=id)
        serializer = studentSerializer(stu, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'completed dtaa updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    def destroy(self, request, pk):
        id = pk
        stu = student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})
    

