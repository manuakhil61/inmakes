from django.http import HttpResponse
from django.shortcuts import render
from . models import Movies

# Create your views here.
def demo(request):
    movie=Movies.objects.all()
    return render(request,'index.html',{'result':movie})