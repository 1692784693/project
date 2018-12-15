# @Time    : 2018/9/28 16:15
# @Author  : pangguoyi
# @File    : urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.place_order),
    url(r'^addorder/$',views.addOrder)


]