from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello world of Django")


def welcome(request):
    return HttpResponse("Hello I am Welcome Page! :) ")

def myname(request):
    return HttpResponse("Hello my name is Kleibert! :D ")
