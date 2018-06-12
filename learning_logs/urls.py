"""定义learning_logs的URL模式"""
from django.urls import re_path, path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #主页
    path(r'', views.index, name='index'),
    #显示主题列表
    path(r'topics/', views.topics, name='topics'),
    #re_path(r'^topics/$', views.topics, name='topics'),
    #特定主题的详细页面
    path(r'topics/<int:topic_id>/', views.topic, name='topic'),
    #re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #用于添加新主题的网页
    path(r'new_topic/', views.new_topic, name='new_topic'),
    #用于添加新条目的页面
    path(r'new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    path(r'edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]