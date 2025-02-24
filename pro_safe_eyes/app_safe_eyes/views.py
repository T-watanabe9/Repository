from typing                     import Any
from django.shortcuts           import render , redirect
from django.views.generic.base  import TemplateView
from django.contrib.auth.views  import LoginView , LogoutView
from django.http                import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


# 未ログインユーザーがURLにアクセスしたときのリダイレクト先
# 新規登録ボタン
# ログインフォーム
# ログアウト時のリダイレクト先
class LoginView(LoginView):
     template_name = 'login.html'
     
     # もしユーザーがログイン済みだったらhome.htmlにリダイレクト。
     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
          if request.user.is_authenticated:
               return redirect("home")
          return super().dispatch(request, *args, **kwargs)



# ホーム画面
class HomeView(LoginRequiredMixin , TemplateView):
     template_name = "home.html"
    #  model = Comment
     
     # クラスベースビューの呼び出し時、クエリセットをログインユーザーのもののみに絞って返す。
    #  def get_queryset(self):
    #        current_user = self.request.user
    #        return Comment.objects.filter(user= current_user) 

