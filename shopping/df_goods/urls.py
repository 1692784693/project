# @Time    : 2018/9/28 16:15
# @Author  : pangguoyi
# @File    : urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^head/$',views.head),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^(\d+)/$',views.detail),
    url(r'^search',views.search)


]