from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def demo(request):
    callHim='Cristano Ronaldo'
    return render(request,'index.html',{'object':callHim})