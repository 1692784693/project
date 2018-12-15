# @Time    : 2018/11/12 15:40
# @Author  : pangguoyi
# @File    : 自媒咖-天天快报.py
import scrapy
from scrapy import Selector,cmdline

from ..items import ScrapynewsItem


class TianTian(scrapy.Spider):
    name = 'TianTian'
    def start_requests(self):

        start_urls=('http://www.zimeika.com/article/lists/tiantian.html?cate_id=69&time_type=&read_order=&type=&author_id=&author_name=&title=&p=',
                    'http://www.zimeika.com/article/lists/tiantian.html?cate_id=68&time_type=&read_order=&type=&author_id=&author_name=&title=&p=',
                    'http://www.zimeika.com/article/lists/tiantian.html?cate_id=67&time_type=&read_order=&type=&author_id=&author_name=&title=&p=')
        for urls in start_urls:
            for i in range(1, 4):
                yield scrapy.Request(url=urls + str(i), callback=self.parse)


    def parse(self, response):
        selector=Selector(response)
        urls = selector.xpath('//div[@class="am-g"]/div/form[@class="am-form"]/table/tbody/tr/td[@class="list-url"]/a/@href')
        classify = selector.xpath('//div[@class="am-g"]/div/form[@class="am-form"]/table/tbody/tr/td[@class="list-url"]/text()')
        for u, c in zip(urls, classify):
            ur = 'http://www.zimeika.com' + u.root
            yield scrapy.Request(url=ur, callback=self.Info, meta={'classify': c.root})


    def Info(self,response):
        selector = Selector(response)
        Title = selector.xpath('//h1[@id="article_title"]/text()')[0].root
        Classify = response.meta['classify'].strip()
        Url = response.url
        Author = selector.xpath('//div[@class="mscc"]/div[@class="article-info "]/span/a/text()')[0].root
        Time = selector.xpath('//div[@class="mscc"]/div[@class="article-info "]/span/text()')[2].root
        Reading = selector.xpath('//div[@class="mscc"]/div[@class="article-info "]/span/text()')[3].root
        Comment = selector.xpath('//div[@class="mscc"]/div[@class="article-info "]/span/text()')[4].root
        contents = selector.xpath('//p[@class="text"]/text()')
        Content = ''
        for content in contents:
            Content += content.root
        zimeitiItem = ScrapynewsItem()
        zimeitiItem['Title'] = Title
        zimeitiItem['Author'] = Author
        zimeitiItem['Url'] = Url
        zimeitiItem['Classify'] = Classify
        zimeitiItem['Reading'] = Reading
        zimeitiItem['Comment'] = Comment
        zimeitiItem['Content'] = Content
        zimeitiItem['Time'] = Time
        yield zimeitiItem

# cmdline.execute('scrapy crawl TianTian'.split())