from django.db import models


class Item(models.Model):
    title = models.CharField(max_length = 200)
    cost = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Produkt {self.title} som kostar {self.cost}kr köpt datumet {self.created}"

class Person(models.Model):
    hireid = models.IntegerField(default=0)
    name = models.CharField(max_length = 200)
    items = models.ManyToManyField(Item, models.DO_NOTHING)#, through="ItemRelationship")
   
    def __str__(self):
        return f"ID: {self.hireid} Namn: {self.name}"

# class ItemRelationship(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     created = models.DateField(auto_now_add=True)
#     number = models.IntegerField(null=True, blank=True)
    

#     def __str__(self):
#         return f"{self.item} - {self.person}"


    


#Namn på det som är köpt
#Vad det som är köpt kostar
#Vilken person som köpt det och dennes ID
#Vilken datum/månad som det är köp
#Hur många av varje sak som är köpt vilken månad av vilken person