from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.
from df_cart.models import CartInfo


def cart(request):
    userId = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=userId)
    return render(request,'df_cart/cart.html',{'carts':carts,'len':len(carts)})

def ifLogin(func):
    def login(request,*args,**kwargs):
        if request.session['user_id']:
            return func(request,*args,**kwargs)
        else:
            resp = HttpResponseRedirect('/user/login/')
    return login

@ifLogin
def add(request,goodsId,goodCount):
    userId = request.session['user_id']
    Carts = CartInfo.objects.filter(user_id=userId).filter(goods_id=goodsId)
    if len(Carts)>0:
        cart = Carts[0]
        cart.count += int(goodCount)
    else:
        cart = CartInfo()
        cart.user_id = userId
        cart.goods_id = goodsId
        cart.count = goodCount
    cart.save()
    carts = CartInfo.objects.filter(user_id=userId)
    return render(request,'df_cart/cart.html',{'carts':carts})
    # return render(request,'df_cart/cart.html')



def deletegood(request,cartId):
     cart = CartInfo()
     cart.id = cartId
     count = CartInfo.delete(cart)
     return JsonResponse({'date':'ok'})