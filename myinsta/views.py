from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image


# Create your views here.

def home(request):
  images = Image.objects.all()
  return render(request, 'instahome.html',{"images":images})



