from django.shortcuts import render
from application.models import summer,monsoon

def x(request):
    return render(request,'index.html')

def y(request):
    data=summer.objects.all()
    return render(request,'summer.html',{'data':data})

def z(request):
    data=monsoon  .objects.all()
    return render(request,'monsoon.html',{'data':data})
