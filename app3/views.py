from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def sujith(request):
    return HttpResponse('<h2>my sis is so beautiful</h2>')

def hari(request):
    return HttpResponse('I am so hungry today')