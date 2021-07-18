from django.contrib import admin
from django.contrib.admin import ModelAdmin

from.models import Item, ItemRelationship
from.models import Person

class ItemAdmin(ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)

class PersonAdmin(ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)

class ItemRelationshipAdmin(ModelAdmin):
    pass
admin.site.register(ItemRelationship)