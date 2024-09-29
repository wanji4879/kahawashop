from django.shortcuts import render
from .models import Kahawaapp

def home(request):
    kahawaapp_data = Kahawaapp.objects.all()
    return render(request, 'home.html', {'kahawaapp_data': kahawaapp_data})
