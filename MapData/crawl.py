# @Time    : 2018/11/26 16:01
# @Author  : pangguoyi
# @File    : crawl.py
import time,csv

import requests
from bs4 import BeautifulSoup

header = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
#翻页判断信息，及获取房源url
def get_url():
    i = 1
    urls = 'https://sz.zu.anjuke.com/?from=navigation'
    while i:
        response = requests.get(urls,headers=header)
        response.encoding='utf-8'
        soup = BeautifulSoup(response.text,'html.parser')
        pag_next = soup.select('a.aNxt')
        if pag_next:
        # if i<10:
            urls = 'https://sz.zu.anjuke.com/fangyuan/p{}/'.format(i)
            i=i+1
            rets = soup.select('div.zu-itemmod')
            for ret in rets:
                title = ret.select('div.zu-info h3 a')[0].text
                url = ret.select('div.zu-info h3 a')[0].get('href')
                loc = ret.select('div.zu-info address')[0].text
                loc1 = ret.select('div.zu-info address a')[0].text
                location = loc.replace(loc1,'').strip()
                price = ret.select('div.zu-side p strong')[0].text
                print(title)
                print(url)
                print(location)
                print(price)

                with open('houseInfo.csv','a',encoding='utf-8',newline='') as f1:
                    csv_write = csv.writer(f1, dialect='excel')
                    csv_write.writerow([title,location,price,url])
            time.sleep(2)
        else:
            break


get_url()
