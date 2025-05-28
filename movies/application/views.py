from django.shortcuts import render

from application.models import tollywood


def x(request):
    return render(request,'index.html')

def y(request):
    data=tollywood.objects.all()
    return render(request,'tollywood.html',{'data':data})

# def fill(request,id):
#     data1=tollywood.objects.get(id=id)
#     return render(request,'filter.html',{'data1':data1})