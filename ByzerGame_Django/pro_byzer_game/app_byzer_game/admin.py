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
     search_fields = ('name', 'category', 'effect_text',  'explain' )
     list_filter = ('category', 'cost' , 'color')
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

admin.site.register(Card , CardAdmin)




# 表示順を変える機能を実装するため、いろいろやってみていた。
from django.views.decorators.http import require_POST
from django.http import JsonResponse
@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name','order', )
    # list_display = ('name', 'increment_button')

    # @admin.display(description='順序を+1')
    # def increment_button(self, obj):
    #     url = reverse('admin:increment_order', args=[obj.pk])
    #     return format_html(
    #     '''
    #     <form method="post" action="{}" style="display:inline;">
    #         <input type="hidden" name="csrfmiddlewaretoken" value="{}" />
    #         <input type="hidden" name="id" value="{}" />
    #         <button type="submit" class="button">+1</button>
    #     </form>
    #     ''',
    #     reverse('admin:race_increment_order'),
    #     '{{ csrf_token }}',  # JavaScript経由の場合はJSで埋め込む、後述
    #     obj.pk)
    
    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [
    #         path(
    #             'increment_order/<int:pk>/',
    #             self.admin_site.admin_view(self.increment_order_view),
    #             name='increment_order',
    #         ),
    #     ]
    #     return custom_urls + urls
    

    # @require_POST
    # def increment_order_view(self, request):
    #     pk = request.POST.get("id")
    #     obj = get_object_or_404(Race, pk=pk)
    #     obj.order += 1
    #     obj.save()
    #     return JsonResponse({'success': True, 'new_order': obj.order})

