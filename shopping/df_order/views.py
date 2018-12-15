from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from df_cart.models import CartInfo
from df_goods.models import GoodsInfo
from df_order.models import OrderInfo, OrderDetailInfo
from df_user.models import UserInfo


def place_order(request):
    orderids = request.GET.getlist('orderid')
    orders = []
    for oid in orderids:
        orders.append(CartInfo.objects.get(id=oid))
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(id = user_id)
    return render(request,'df_order/place_order.html',{'orderlist':orderids,'user':user})

# def pay(request):
#     return render(request,'df_order/pay.html')

def site(request):
    return render(request,'df_user/user_center_site.html')

def addOrder(request):
    orderids = request.session.get('orderids')
    order = OrderInfo()
    oOder = OrderInfo.objects.all().order_by('-oid')[0:1]
    if len(oOder)==0:
        order.oid = 1
    else:
        order.oid = int(oOder[0].oid)+1
    order.odate = datetime.now()
    order.oIsPay = 0
    order.ototal = request.POST.get('total')
    order.oaddress = request.POST.get('address')
    order.user_id = request.session.get('user_id')
    order.zhifu = request.POST.get('zhifu')
    order.save()
    for oid in orderids:
        cartInfo = CartInfo.objects.get(id = oid)
        good = GoodsInfo.objects.get(id = cartInfo.goods_id)
        if cartInfo.count > good.gkucun:
            return JsonResponse({'status':2})

        detail = OrderDetailInfo()
        detail.price = good.gprice
        detail.count = cartInfo.count
        detail.goods_id = good.id
        detail.order_id = order.oid
        detail.save()
    return JsonResponse({'status':1})

