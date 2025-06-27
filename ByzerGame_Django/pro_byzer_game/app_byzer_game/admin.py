from django.contrib import admin
from .models import Card
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
class CardAdmin(SortableAdminMixin, admin.ModelAdmin):
     list_display = ('id' , 'name' , 'category' ,  'cost' , 'color' , 'race', 'priority')
     search_fields = ('name', 'category' , 'effect_text', 'race', 'explain' )
     list_filter = ('category', 'cost' , 'color')

admin.site.register(Card , CardAdmin)
