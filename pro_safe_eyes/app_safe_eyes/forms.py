from django import forms
from .models import Comment


# コメント用フォーム。
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['datetime' , 'physical_health' , 'mental_health' , 'busy' , 'content']
        widgets = {

            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'physical_health': forms.RadioSelect(),  
            'mental_health': forms.RadioSelect(),  
            'busy': forms.RadioSelect(),
            # ↓content のサイズを指定したいとき。
            # 'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  
        }