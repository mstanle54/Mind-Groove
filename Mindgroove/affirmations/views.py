import imp
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'hello.html')

def affirmations(request):
    return render(request, 'affirmationsBox.html')    
