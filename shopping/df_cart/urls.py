# @Time    : 2018/9/28 16:16
# @Author  : pangguoyi
# @File    : urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.cart),
    url(r'^add(\d+)_(\d+)/$',views.add),
    # url(r'^edit(\d+)_(\d+)/$',views.edit),
    url(r'^delete/(\d+)/$',views.deletegood),



]