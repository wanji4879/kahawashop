from django.shortcuts import render
from django.http import HttpResponse
from .models import Kahawaapp  



def home(request): 
    kahawaapp_data = Kahawaapp.objects.all() 
    return render(request, 'home.html',{'kahawaapp_data': kahawaapp_data})