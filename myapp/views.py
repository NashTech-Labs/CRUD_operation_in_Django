import json
# import re
# from types import NoneType
from urllib import request, response
from django import views
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse , get_object_or_404 
from requests import delete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeesSerializer
from django.http import HttpResponse,JsonResponse

from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .import models
from .models import employees
import urllib.request
import urllib

from myapp import serializers


# Create your views here.
def index(request):
    return HttpResponse("This is homepage")
def about(request):
    return HttpResponse("This is about")
def contact(request):
    return HttpResponse("This is contact")
def service(request):
    return HttpResponse("This is service")

# Info of serializer to convert the data in json format 

# class employeesList(viewsets.ModelViewSet):
#     queryset=models.employees.objects.all()
#     serializer_class=serializers.employeesSerializer

class employeesList(APIView):
    def get (self, request, id=None):
     if id:
        employees1=employees.objects.get(id=id)
        serializer=employeesSerializer(employees1)
        return Response(serializer.data)

     employees2=employees.objects.all()
     serializer=employeesSerializer(employees2, many=True)
     return Response(serializer.data)

    def post(self,request):
     if request.method == 'POST':
        data=JSONParser().parse(request)
        serializer=employeesSerializer(data=data)
        

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =201)
        return Response(serializer.errors, status =400)

    def put(self,request):
     if request.method == 'PUT':
        data=JSONParser().parse(request)
        serializer=employeesSerializer(data=data)
        data={}
           
        if serializer.is_valid():
            serializer.save()
            data["success"]="update successful"
            return Response(serializer.data,status =201)
        return Response(serializer.errors, status =400)

    def delete(self,request, id=None):
        employees1=get_object_or_404(employees, id=id)
        employees1.delete()
        return Response({"status":"success","data":"deleted successfully"})
        # serializer=employeesSerializer(data=data)
        

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status =201)
        # return Response(serializer.errors, status =400)   

    


    # def delete(self,request, ):

    #     if request.method == "DELETE":
            
    #         employees.delete()
    #         return HttpResponse(status =204)
       
     
