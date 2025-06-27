from django.db import models
from django.contrib import admin
from django.forms import Textarea
from .models import Card
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
class CardAdmin(SortableAdminMixin, admin.ModelAdmin):
     list_display = ('id' , 'name' , 'category' ,  'cost' , 'color' , 'race' , 'priority')
     search_fields = ('name', 'category' , 'effect_text', 'race', 'explain' )
     list_filter = ('category', 'cost' , 'color')
     formfield_overrides = {
         models.TextField: {'widget': Textarea(attrs={
    'style': 'min-height: 200px; max-height: none !important; width: 90%;',
})},
     }

admin.site.register(Card , CardAdmin)
