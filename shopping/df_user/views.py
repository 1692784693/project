from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from df_user.models import UserInfo
from df_order.models import OrderInfo,OrderDetailInfo
from  df_goods.models import GoodsInfo



# Create your views here.
def register(request):
    return render(request,'df_user/register.html')

def login(request):
    return render(request,'df_user/login.html')

def register_handle(request):
    if request.method == 'POST':
        u_user_name = request.POST.get('user_name')
        u_pwd =request.POST.get('pwd')
        u_cpwd =request.POST.get('cpwd')
        u_email =request.POST.get('email')
        u_allow =request.POST.get('allow')
    users = UserInfo(uname=u_user_name,upwd=u_pwd,uemail=u_email)
    users.save()
    # return render(request,'df_user/login.html')
    return HttpResponseRedirect('/user/login/')

def login_handle(request):
    uName = request.POST.get('username')
    uPwd = request.POST.get('pwd')

    user = UserInfo.objects.filter(uname=uName)
    if user.count() == 1:
        if user[0].upwd == uPwd:
            request.session['user_name'] = uName
            request.session['user_id'] = user[0].id
            return HttpResponseRedirect('/')
        else:
            return render(request, 'df_user/login.html', {'error_name': 0, 'error_pwd': 1})
    else:
        return render(request, 'df_user/login.html', {'error_name': 1, 'error_pwd': 0})
    # return render(request,'df_goods/index.html')

def register_exist(request):
    uName = request.GET.get('uname')
    user = UserInfo.objects.filter(uname=uName)
    return HttpResponse(user.count())

def info(request):
    return render(request,'df_user/user_center_info.html',{'goods_list':GoodsInfo.objects.all()})

def user_center_order(request):
    return render(request,'df_user/user_center_order.html',{'orderlist':OrderInfo.objects.all(),'orderdetailinfo_set':OrderDetailInfo.objects.all()})

def site(request):
    userId = request.session['user_id']
    u_shou = request.POST.get('ushou')
    u_address = request.POST.get('uaddress')
    u_youbian = request.POST.get('uyoubian')
    u_phone = request.POST.get('uphone')
    userin =UserInfo()
    userin.id = userId
    userin.ushou=u_shou
    userin.uaddress = u_address
    userin.uyoubian = u_youbian
    userin.uphone = u_phone
    userin.save()

    user = UserInfo.objects.filter(id=userId)
    return render(request,'df_user/user_center_site.html',{'user':user})


def logout(request):
    request.session['user_name']=''
    return HttpResponseRedirect('/')

