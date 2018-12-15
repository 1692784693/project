from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from df_goods.models import TypeInfo,GoodsInfo

# Create your views here.
def index(request):
    # fruit2 = GoodsInfo.objects.filter(id=1).filter(id=2).filter(id=3).filter(id=4)
    # fruit = GoodsInfo.objects.filter(id=1).filter(id=2).filter(id=3).filter(id=4)
    # fruit2 = GoodsInfo.objects.all()[0:4]
    # fruit = GoodsInfo.objects.all()[0:4]
    # fish2 = GoodsInfo.objects.all()[4:8]
    # fish = GoodsInfo.objects.all()[4:8]
    fruit = GoodsInfo.objects.filter(gtype=2).order_by('-gclick')[0:4]
    fruit2 = GoodsInfo.objects.filter(gtype=2).order_by('-gclick')[0:4]
    fish = GoodsInfo.objects.filter(gtype=4).order_by('-gclick')[0:4]
    fish2 = GoodsInfo.objects.filter(gtype=4).order_by('-gclick')[0:4]

    # title = GoodsInfo.objects.filter(gtitle__contains=request.GET)
    return render(request,'df_goods/index.html',{ 'page_name':1,
                                                     'fruit2':fruit2,
                                                     'fruit':fruit,
                                                     'fish2':fish2,
                                                    'fish':fish })

def head(request):
    return redirect(request,'df_goods/index.html')

def list(request,typeid,pagId,sortId):
    goods=GoodsInfo.objects.filter(gtype_id=typeid)
    if sortId == '2':
        goods = goods.order_by('gprice')
    if sortId == '3':
        goods = goods.order_by('-gclick')
    pageGood = Paginator(goods, 2).page(pagId)
    pindexlist = Paginator(goods, 2).page_range
    newgoods = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')[0:3]
    return render(request,'df_goods/list.html',{'typeid':typeid,'goodList':pageGood,'sort':sortId,
                                                'pindexlist':pindexlist,
                                                'newgood':newgoods})

def detail(request,gi):
    g=GoodsInfo.objects.get(id = gi)
    g.gclick +=1
    g.save()
    newgood = GoodsInfo.objects.filter(gtype_id=g.gtype_id).order_by('-id')[0:3]
    goodtype = g.gtype
    # g = GoodsInfo.objects.raw('SELECT * FROM df_goods_goodsinfo where id='+gi)[0]
    # g = GoodsInfo.objects.all()[gi-1]
    return render(request,'df_goods/detail.html',{'g':g,'newgood':newgood,'goodtype':goodtype,})


def search(request):
    gfind = request.GET.get('q')
    ufind = GoodsInfo.objects.filter(gtitle__contains=gfind)
    # newgoods = GoodsInfo.objects.filter(gtype_id=ufind[0].gtype_id).order_by('-id')[0:3]
    return render(request,'df_goods/list.html',{'goodList':ufind})