from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, Manasvi You are Doing Great Keep It Up!')

