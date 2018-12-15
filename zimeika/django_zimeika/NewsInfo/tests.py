from django.test import TestCase
import requests
from bs4 import BeautifulSoup
# Create your tests here.

urls=['https://www.zimeika.com/article/lists/toutiao.html?cate_id=69&time_type=&read_order=&type=&author_id=&author_name=&title=&p=',
      'https://www.zimeika.com/article/lists/toutiao.html?cate_id=68&time_type=&read_order=&type=&author_id=&author_name=&title=&p=',
      'https://www.zimeika.com/article/lists/toutiao.html?cate_id=67&time_type=&read_order=&type=&author_id=&author_name=&title=&p=',]

def TouTiao():
    for url in urls:
        for i in range(1,4):
            result=requests.get(url+str(i))
            soup = BeautifulSoup(result.text,'html.parser')
            results = soup.select('table tbody tr')
            for res in results:
                title=res.select('td.list-url a')
                author=res.select('td.list-url td a')

            print(results)


TouTiao()
def aaabbb():
    url ='http://www.zimeika.com/article/detail/toutiao.html?id=20438331'
    res = requests.get(url=url)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.select('h1#article_title')[0].text
    Content = soup.select('span#content div')[0].text
    print(title,Content)


# aaabbb()