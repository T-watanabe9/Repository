from django import forms
from django.db import models
from django.contrib import admin
from django.forms import Textarea
from .models import Card
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

# カスタムフォームの定義
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'effect_text': Textarea(attrs={
                'style': 'min-height: 200px; max-height: none !important; ',
                'rows': 20,  # rowsはstyleではなく属性として指定
            }),
        }

class CardAdmin(SortableAdminMixin, admin.ModelAdmin):
     form = CardForm
     list_display = ('id' , 'name' , 'category' ,  'cost' , 'color' , 'race' , 'priority')
     search_fields = ('name', 'category' , 'effect_text', 'race', 'explain' )
     list_filter = ('category', 'cost' , 'color')
     

admin.site.register(Card , CardAdmin)
