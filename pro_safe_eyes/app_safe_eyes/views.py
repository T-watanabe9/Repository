from typing                     import Any
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.shortcuts           import render , redirect
from django.views.generic.base  import TemplateView
from django.views.generic       import ListView , UpdateView
from django.views.generic.edit  import CreateView , DeleteView
from django.contrib.auth.views  import LoginView , LogoutView
from django.http                import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from .models                    import Comment
from .forms import CommentCreateForm



# Create your views here.


# ログイン画面
# ログアウト時のリダイレクト先
# 未ログインユーザーがURLにアクセスしたときのリダイレクト先
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
     


# コメントリスト画面
class CommentListView(LoginRequiredMixin , ListView):
     template_name = "models/comment_list.html"
     model = Comment
     # paginate_by = 5

     # ビューが呼び出されたとき
     def get_queryset(self):
           # フロントに渡すクエリセットをログイン済ユーザーのみに絞る。
           user = self.request.user
           return Comment.objects.filter(user= user) 


# コメント作成画面
class CommentCreateView(LoginRequiredMixin , CreateView):
     template_name = "models/comment_create.html"
     model = Comment
     form_class = CommentCreateForm
     success_url = reverse_lazy('comment')
     # fields = ['physical_health' , 'mental_health' , 'content']
     
     # フォーム入力時に呼び出し。
     def form_valid(self, form: BaseModelForm) :
          # 新規作成フォームにて、userフィールドは必ずログインユーザーとする。
          form.instance.user = self.request.user
          return super().form_valid(form)


# コメント編集画面
class CommentUpdateView(LoginRequiredMixin , UpdateView):
     template_name = "models/comment_update.html"
     model = Comment
     pass
