from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def wish(Request):
    return HttpResponse('hi,i am here')
