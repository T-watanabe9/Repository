from django.contrib import admin
from .models import Card
from django.forms import Textarea
from django.db import models

# Register your models here.
class CardAdmin(admin.ModelAdmin):
     list_display = ('id' , 'name' , 'category' ,  'cost' , 'color' , 'race')
     search_fields = ('name', 'category' , 'effect_text', 'race', 'explain' )
     list_filter = ('category', 'cost' , 'color')

admin.site.register(Card , CardAdmin)
