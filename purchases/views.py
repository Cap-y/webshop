from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render (HttpResponse)

def items(request):
   # return HttpResponse('Test')
    context = {"Albin": "Test"}
    return render(request, 'purchases/test.html', context)
