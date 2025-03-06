from typing                     import Any
from django.shortcuts           import render , redirect
from django.views.generic.base  import TemplateView
from django.views.generic       import ListView
from django.contrib.auth.views  import LoginView , LogoutView
from django.http                import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from .models                    import Comment



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

# コメント画面。
class CommentListView(LoginRequiredMixin , ListView):
     # template_name = "comment.html"
     template_name = "models\comment_list.html"
     model = Comment
     # paginate_by = 5

     # ビューが呼び出されたとき
     def get_queryset(self):
           # フロントに渡すクエリセットをログイン済ユーザーのみに絞る。
           user = self.request.user
           return Comment.objects.filter(user= user) 
     
     # # ビューが呼び出されたとき：getリクエスト
     # def get(self, request, *args, **kwargs):
     #      return super().get(self, request, *args, **kwargs)
     
     # # 検索ボタンを押したとき：postリクエスト
     # def post(self, request, *args, **kwargs):
     #      # return super().post(self, request, *args, **kwargs)
     #      print("コメントビュー!post関数!")
     #      dic = test_search(request)
     #      print(dic)
     #      return JsonResponse({'message': 'データが正常に保存されました。'})

