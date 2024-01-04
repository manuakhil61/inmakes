from django.shortcuts import render
from . models import pics
# Create your views here.

def demo(request):
    obj=pics.objects.all()
    return render(request,"index.html",{'result':obj})