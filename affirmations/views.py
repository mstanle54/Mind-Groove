import imp
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def loginPage(request):
    context = {}
    return render(request, 'login_register.html', context)

def home(request):
    return render(request, 'home.html')

def affirmations(request):
    return render(request, 'affirmationsBox.html')    
