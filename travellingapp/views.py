from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def fun(request):
    return render(request,"home.html",{'name':'Addition'})

def addition(request)
    return render(request,"result.html")

