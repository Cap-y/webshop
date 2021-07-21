from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from purchases.models import Item, ItemRelationship, Person

def index(request):
    return render (HttpResponse)

def items(request):
    person = Person.objects.all()
    items = Item.objects.all()
    purchases = ItemRelationship.objects.all()
    context = {"items": items,  "persons": person, "purchases": purchases}
    return render(request, 'purchases/items.html', context)
            

def purchased(request):
    person = Person.objects.all()
    purchases = ItemRelationship.objects.all()
    context = {"purchases": purchases,  "persons": person} 
    return render(request, 'purchases/purchased.html', context)