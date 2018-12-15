# @Time    : 2018/9/28 16:15
# @Author  : pangguoyi
# @File    : urls.py
from django.conf.urls import url,include
from df_user import views


urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login_handle/$',views.login_handle),
    url(r'^info/',views.info),
    url(r'^user_center_order&(/d+)/$',views.user_center_order),
    url(r'^site/$',views.site),
    url(r'^register_exist/$',views.register_exist),
    url(r'^logout/$',views.logout),

]