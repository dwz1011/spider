# -*- coding:utf-8 -*-

from common import *
import re

def sitemap_spider(url):
	sitemap = download(url)
	req = '<loc>(.*?)</loc>'
	links = re.findall(req, sitemap)
	for link in links:
		html = download(link)
    	
if __name__ == '__main__':
	sitemap_spider('http://example.webscraping.com/sitemap.xml')