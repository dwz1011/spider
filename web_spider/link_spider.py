# -*- coding:utf-8 -*-

from common import *
import re

def get_links(html):
	reg = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	return reg.findall(html)

def link_spider(seed_url, link_regex):
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		for link in get_links(html):
			if re.match(link_regex, link):
				crawl_queue.append(link)

if __name__ == '__main__':
    link_spider('http://example.webscraping.com', '/(index|view)')