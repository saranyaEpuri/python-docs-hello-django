from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello everyone! Our training has come to an end. Wishing everyone the best for future.")
