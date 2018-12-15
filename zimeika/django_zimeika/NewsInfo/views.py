from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import  HttpResponseRedirect

# Create your views here.

from NewsInfo.models import ZiMeiKaInfo


def TouTiao(request):
    contact_list = ZiMeiKaInfo.objects
    contacts=pages(request,contact_list)
    return render(request,'index.html',{'contacts': contacts})

def content(request,url):
    c=request.GET['id']
    urls=url+'?id='+c

    Info2= ZiMeiKaInfo.objects.filter(Url=urls.strip('/'))[0]

    return render(request,'content.html',{'Info2':Info2})

def search(request):
    result = request.POST.get('search')
    contacts_list = ZiMeiKaInfo.objects.filter(Title__contains = result)
    Filter_search=pages(request,contacts_list)
    return render(request,'index.html',{'contacts':Filter_search})

def field(request,num):
    if num=='0':
        contacts_list=ZiMeiKaInfo.objects.filter()
    if num=='69':
        contacts_list=ZiMeiKaInfo.objects.filter(Classify='[法律]')
    if num=='68':
        contacts_list=ZiMeiKaInfo.objects.filter(Classify='[技术]')
    if num=='67':
        contacts_list=ZiMeiKaInfo.objects.filter(Classify='[十九大]')
    if num=='66':
        contacts_list=ZiMeiKaInfo.objects.filter(Classify='[移民]')
    contacts = pages(request,contacts_list)
    return render(request,'index.html',{'contacts': contacts})

def pages(request,contact_list):
    paginator = Paginator(contact_list,15)  # Show 25 contacts per page
    page = request.GET.get('page',1)

    contacts = paginator.page(page)
    return contacts