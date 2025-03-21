from django import forms
from .models import Comment


# コメント作成フォーム。
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['physical_health' , 'mental_health' , 'content']
        widgets = {
            'physical_health': forms.RadioSelect(),  
            'mental_health': forms.RadioSelect(),  
            # content のサイズを指定したいとき。
            # 'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  
        }