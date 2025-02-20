from django.shortcuts import render
from django.views.generic       import ListView

# Create your views here.

# ホーム画面
class HomeView(ListView):
     template_name = "home.html"
    #  model = Comment
     
     # クラスベースビューの呼び出し時、クエリセットをログインユーザーのもののみに絞って返す。
    #  def get_queryset(self):
    #        current_user = self.request.user
    #        return Comment.objects.filter(user= current_user) 