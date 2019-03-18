# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PropertiesPipeline(object):

	'''
	# 初始化操作 一般用于打开文件
	def __init__(self):
		self.file.open('xxx.json', 'wb')

	# spider 开启时调用
	def open_spider(self):
		pass

	# spider 关闭时调用
	def close_spider(self):
		self.file.close()

	# 必须函数 处理数据
    def process_item(self, item, spider):
    	self.file.write(xx)
        return item
	'''

	# 推荐方式
	def process_item(self, item, spider):
    	with open('xx.json', 'a', encoding='utf-8') as fw:
    		pass
    	
        return item