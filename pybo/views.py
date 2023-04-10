from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request) :
    return HttpResponse("Hello World!")

def create(request) :
    return HttpResponse("Create!")

def read(request, id) :
    return HttpResponse("Read!" + id)