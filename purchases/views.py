from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.http import HttpResponse
from django.templatetags.static import static
from purchases.models import Item, ItemRelationship, Person

def index(request):
    return render (HttpResponse)

def items(request):
    default = static('webshop/default.jpg')
    person = Person.objects.all()
    items = Item.objects.all()
    purchases = ItemRelationship.objects.all()
            
    context = {"items": items,  "persons": person, "purchases": purchases}
    return render(request, 'purchases/items.html', context)
            

def purchased(request):
    PurchaseForm = modelform_factory(ItemRelationship, exclude=[])
    form = PurchaseForm(request.POST)
    person = Person.objects.all()
    purchases = ItemRelationship.objects.all()
    if request.method == "POST":
        purchase = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchased")
        else:
            form = PurchaseForm()
    context = {"purchases": purchases,  "persons": person, "form": form} 
    return render(request, 'purchases/purchased.html', context)