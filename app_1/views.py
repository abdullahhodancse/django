from django.shortcuts import render
from django.http import HttpResponse

def course(request):
    return HttpResponse("This is the course page")

def about(request):
    return HttpResponse("This is a aout")

def home(request):
    return HttpResponse("This is home page of course")    
