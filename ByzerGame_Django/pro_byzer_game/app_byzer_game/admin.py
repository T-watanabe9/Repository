from django import forms
from django.db import models
from django.contrib import admin
from django.forms import Textarea
from .models import Card, Race
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
# カードモデルのAdminサイト
class CardAdmin(SortableAdminMixin, admin.ModelAdmin):
     form = CardForm
     list_display = ('get_prio', 'id' , 'name' , 'category' ,  'cost' , 'color' , 'priority', )
     list_display_links = ('id',)  # idをリンクにする
     search_fields = ('name', 'category' , 'effect_text',  'explain' )
     list_filter = ('category', 'cost' , 'color')

admin.site.register(Card , CardAdmin)


class RaceAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Race , RaceAdmin)
