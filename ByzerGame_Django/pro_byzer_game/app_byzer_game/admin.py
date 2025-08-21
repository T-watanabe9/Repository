from django import forms
from django.db import models
from django.contrib import admin
from django.contrib import messages
from django.forms import Textarea
from django.urls import path , reverse
from django.utils.html import format_html
from .models import Card, Race
from adminsortable2.admin import SortableAdminMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.admin import SimpleListFilter

# Register your models here.

# カスタムフォームクラス。
# 新規作成＆編集時のtextAreaを広くする。
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

# カスタムフィルタークラス。
class AnyRaceFilter(SimpleListFilter):
    title = 'いずれかの系統 (race1〜3)'
    parameter_name = 'any_race'

    def lookups(self, request, model_admin):
        races = Race.objects.all()
        return [(race.id, race.name) for race in races]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                models.Q(race1__id=self.value()) |
                models.Q(race2__id=self.value()) |
                models.Q(race3__id=self.value())
            )
        return queryset
    
# カードモデルのAdminサイト
@admin.register(Card)
class CardAdmin(admin.ModelAdmin): # SortableAdminMixin, 
     form = CardForm
     # list_display = ('get_prio', 'id' , 'name' , 'get_race' , 'priority', )
     list_display = ('id' , 'name' , 'get_race' , 'expansion', 'priority')
     list_display_links = ('id',)  # idをリンクにする
     search_fields = ('name', 'category', 'effect_text',  'explain' )
     list_filter = ('category', 'cost' , 'color',  AnyRaceFilter , 'expansion')
     ordering = ('priority',)
     actions = ['add_da_yo_to_name']

     @admin.action(description='選択したカードの名前を「名前+だよ。」に変更')
     def add_da_yo_to_name(self, request, queryset):
         updated_count = 0
         for card in queryset:
             card.name = f"{card.name}だよ。"
             card.save()
             updated_count += 1
         
         self.message_user(
             request, 
             f"{updated_count}件のカードの名前を「だよ。」付きに変更しました。", 
             messages.SUCCESS
         )





# 表示順を変える機能を実装するため、いろいろやってみていた。
from django.views.decorators.http import require_POST
from django.http import JsonResponse
@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name','order', )
    ordering = ('order',)
    actions = ['order_up' , 'order_down']


    @admin.action(description='選択したカードの表示順を+1')
    def order_up(self, request, queryset):
        count = 0
        for race in queryset:
            race.order += 1
            race.save()
            count += 1
        
        self.message_user(
            request, 
            f"{count}件のraceの優先順位を+1しました。", 
            messages.SUCCESS
        )

    
    @admin.action(description='選択したカードの表示順を+1')
    def order_down(self, request, queryset):
        count = 0
        for race in queryset:
            race.order -= 1
            race.save()
            count += 1
        
        self.message_user(
            request, 
            f"{count}件のraceの優先順位を-1しました。", 
            messages.SUCCESS
        )

    


