"""
URL configuration for pro_safe_eyes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_safe_eyes import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(), name='login'),
    path('home', views.HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('comment/', views.CommentListView.as_view(), name='comment'),
    path('comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<uuid:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<uuid:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
