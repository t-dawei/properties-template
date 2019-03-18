# -*- coding: utf-8 -*-
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

'''
scrapy 存在自动去重机制
'''

'''
LinkExtractor构造器参数：
allow :接收一个正则表达式或一个正则表达式列表，提取绝对url与正则表达式匹配的链接。如果该参数为空（默认），就提取全部链接。
deny:接收一个正在则表达式或一个正则表达式列表，与allow相反，排除绝对url与正则表达式匹配的链接。
allow_domains:接收一个域名或一个域名列表，提取到指定域的链接
deny_domain:与allow_domains相反，排除指定域的链接
restrict_paths:接收一个XPath表达式或一个XPath表达式列表，提取XPath表达式选中区域下的链接
restrict_css:接收一个CSS选择器或一个CSS选择器列表，提取CSS选择器选中区域下的链接
tags:接收一个标签/标签列表，提取指定标签内的链接，默认为 ['a','area']
attrs:接收一个属性/属性列表，提取指定属性内的链接，默认为 ['href']
process_value:接收一个形如func(value)的回调函数，如果传递了该参数，LinkExtractor将调用该回调函数对提取的每一个链接进行处理，回调函数
'''
'''
# 从页面需要提取的url 链接(link)
links = LinkExtractor(allow=r"")
# 设置解析link的规则，callback是指解析link返回的响应数据的的方法
rules = [Rule(link_extractor=links, callback="parseContent", follow=True)]
'''

class XxSpider(CrawlSpider):
    name = 'xx'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    rules = (
        # 水平爬取
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"next")]')),
        # 垂直爬取
        Rule(LinkExtractor(restrict_xpaths='//*[@itemprop="url"]'), callback='parse_item'),
    )

    def parse_item(self, response):
        # 定义loader 装饰器
        loader = ItemLoader(item=PropertiesItem(), response=response)

        loader.add_value('link', response.url)

        loader.add_xpath('text', 'xpath表达式', MapCompose(unicode.strip, unicode.titile), Join())

        return loader.load_item()

'''
# 需要实例化ItemLoader， 注意第一个参数必须是实例化的对象...
atricleItemLoader = ItemLoader(item = articleDetailItem(), response=response)
# 调用xpath选择器，提取title信息
atricleItemLoader.add_xpath('title', '//div[@class="entry-header"]/h1/text()')
# 调用css选择器，提取praise_nums信息
atricleItemLoader.add_css('praise_nums', '.vote-post-up h10::text')
# 直接给字段赋值，尤其需要注意，不管赋值的数据是什么，都会自动转换成list类型
atricleItemLoader.add_value('url', response.url)
'''