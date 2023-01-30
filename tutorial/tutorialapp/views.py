from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def html(request):
    return render(request,'html.html')

def css(request):
    return render(request,'css.html')

def js(request):
    return render (request,'js.html')

def python(request):
    return render(request,'python.html')

def htmldetail(request):
    return render(request,'htmldetail.html')

def cssdetail(request):
    return render(request,'cssdetail.html')

def pythondetail(request):
    return render(request,'pythondetail.html')