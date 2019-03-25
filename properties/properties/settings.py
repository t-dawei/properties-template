# -*- coding: utf-8 -*-

# Scrapy settings for properties project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'properties'

SPIDER_MODULES = ['properties.spiders']

NEWSPIDER_MODULE = 'properties.spiders'

HTTPERROR_ALLOWED_CODES = [403]

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'properties.middlewares.RandomUserAgentMiddlware': 333,
    'properties.middlewares.MyjsSpiderMiddleware': 543,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   	'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
 	# 'Cookie': '__cfduid=d1459fffcf65efcaf0403f0c9b38ca9ca1547803494; __utmz=200109231.1547803630.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmz=28588142.1547803645.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ym_uid=1547804002328698795; _ym_d=1547804002; __utmc=200109231; _ym_isad=2; cf_clearance=4d0f24b1af5c7a39f25f80cf434ee7f9072b8b52-1548052119-300-150; __utma=200109231.530814173.1547803630.1548039901.1548052250.4; __utmt=1; __utmb=200109231.1.10.1548052250; PHPSESSID=d67725c28ac0e05d09abf0b75ea7481e; __utma=28588142.1144334430.1547803645.1547803645.1548052334.2; __utmc=28588142; __utmb=28588142.4.10.1548052334'
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:

# 当DOWNLOAD_DELAY = 0 生效 默认为8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 当DOWNLOAD_DELAY > 0 生效 默认为8
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'properties.pipelines.PropertiesPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
