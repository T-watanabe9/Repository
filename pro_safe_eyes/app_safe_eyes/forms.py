from django import forms
from .models import Comment


# コメント用フォーム。
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['datetime' , 'physical_health' , 'mental_health' , 'content']
        widgets = {
            'physical_health': forms.RadioSelect(),  
            'mental_health': forms.RadioSelect(),  
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
            # ↓content のサイズを指定したいとき。
            # 'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  
        }