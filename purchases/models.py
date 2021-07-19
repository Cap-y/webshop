from django.db import models
from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length = 200)
    cost = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to= settings.MEDIA_ROOT, null=True, blank=True)

    def __str__(self):
        return f"Produkt {self.title} som kostar {self.cost}kr inlagt {self.created}"

class Person(models.Model):
    hireid = models.IntegerField(default=0)
    name = models.CharField(max_length = 200)
    items = models.ManyToManyField(Item, through="ItemRelationship")
   
    def __str__(self):
        return f"ID: {self.hireid} Namn: {self.name}"

class ItemRelationship(models.Model):
    persons = models.ForeignKey(Person, on_delete=models.CASCADE)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    buydate = models.DateField(auto_now_add=True)
    number = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.persons} köpt {self.items} antal {self.number} vid datum {self.buydate}"


    


#Namn på det som är köpt
#Vad det som är köpt kostar
#Vilken person som köpt det och dennes ID
#Vilken datum/månad som det är köp
#Hur många av varje sak som är köpt vilken månad av vilken person