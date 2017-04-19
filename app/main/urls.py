from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^profile/create$', views.profile_create, name='profile_create'),
    url(r'^profile/save$', views.profile_save, name='profile_save'),

    url(r'^book/$', BookList.as_view(), name='book_list'),   # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除

    url(r'^book/(?P<book_id>\d+)/impression/$', ImpressionList.as_view(), name='impression_list'),
    url(r'^book/(?P<book_id>\d+)/impression/add/$', views.impression_edit, name='impression_add'),
    url(r'^book/(?P<book_id>\d+)/impression/mod/(?P<impression_id>\d+)/$', views.impression_edit, name='impression_mod'),
    url(r'^book/(?P<book_id>\d+)/impression/del/(?P<impression_id>\d+)/$', views.impression_del, name='impression_del'),

    url(r'^regist/$', views.regist, name='regist'),
    url(r'^regist_save/$', views.regist_save, name='regist_save'),

    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'main/index.html'}, name='logout'),
]
