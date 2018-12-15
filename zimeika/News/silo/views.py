import datetime

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.http import  HttpResponseRedirect

# Create your views here.

# from NewsInfo.models import ZiMeiKaInfo
from silo.models import NewsInfo

#主界面
def TianTian(request):
    contact_list = NewsInfo.objects.filter()
    contacts=pages(request,contact_list)
    return render(request,'index.html',{'contacts': contacts})

#内容
def content(request,uid):
    Info2= NewsInfo.objects.filter(id=uid)[0]
    return render(request,'content.html',{'Info2':Info2})

#搜索
def search(request):
    result1 = request.POST.get('search')
    result2 = request.POST.get('cate_id')
    result3 = request.POST.get('time_type')
    result4 = request.POST.get('read_order')

    contacts_list = NewsInfo.objects.filter(Title__contains = result1).filter(Classify=field[result2])
    Filter_search=pages(request,contacts_list)
    return render(request,'index.html',{'contacts':Filter_search})

#领域
def field(request,num):
    if num=='0':
        contacts_list=NewsInfo.objects.filter()
    if num=='69':
        contacts_list=NewsInfo.objects.filter(Classify='[二手房]')
    if num=='68':
        contacts_list=NewsInfo.objects.filter(Classify='[家装]')
    if num=='67':
        contacts_list=NewsInfo.objects.filter(Classify='[园艺]')
    contacts = pages(request,contacts_list)
    return render(request,'index.html',{'contacts': contacts})

#翻页函数代码
def pages(request,contact_list):
    paginator = Paginator(contact_list,15)  # Show 25 contacts per page
    page = request.GET.get('page',1)

    contacts = paginator.page(page)
    return contacts

