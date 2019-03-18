#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: T
# @DateTime: 2019-03-10

# 导入scrapy 基础框架
import scrapy
# 导入爬取规则 rules 字段用
from scrapy.linkextractors import LinkExtractor
# 导入父类CrawlSpider 和字段Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入item
from properties.items import PropertiesItem
# 导入item 装饰器
from scrapy.loader import ItemLoader
# 导入装饰器处理函数
from scrapy.loader.processors import MapCompose, Join
# 导入bs4页面解析库
from bs4 import BeautifulSoup
# 导入时间库
import datetime

class XxSpider(CrawlSpider):
    name = 'vul_bulletins'
    allowed_domains = ['vulners.com']
    base_url = 'https://vulners.com/search?query=type:*'
    url = []
    for i in range(0, 20, 20):
    	url.append(base_url + '&skip=' + str(i))
    start_urls = url

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="vulners-card-text"]'), callback='parse_item', follow=False),
    )

    def parse_link(self, links):
        for link in links:
            print(link)

    def parse_item(self, response):
        # 定义loader 装饰器
        print(response.url)
        # 定义loader 装饰器
        loader = ItemLoader(item=PropertiesItem(), response=response)

        loader.add_value('link', response.url)

        loader.add_xpath('text', '//div[@class="vulners-card-text"]//text()', MapCompose(str.strip), Join())

        return loader.load_item()