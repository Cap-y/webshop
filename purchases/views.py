from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from purchases.models import Item

def index(request):
    return render (HttpResponse)

def items(request):
    return render(request, 'purchases/items.html', 
            {"item": Item.objects.all()})
