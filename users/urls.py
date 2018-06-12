"""定义users的URL模式"""
from django.urls import re_path, path
from django.contrib.auth.views import login
from . import views

app_name = 'users'
urlpatterns = [
    #登陆页面
    path(r'login/', login, {'template_name':'users/login.html'}, name='login'),
    #注销
    path(r'logout/', views.logout_view, name='logout'),
    #注册页面
    path(r'register/', views.register, name='register'),
    ]