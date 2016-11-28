# -*- coding:utf-8 -*-

from common import *
import re
import urlparse

def get_links(html):
	reg = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	return reg.findall(html)

def link_spider(seed_url, link_regex):
	crawl_queue = [seed_url]
	seen = set(crawl_queue)
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		for link in get_links(html):
			if re.match(link_regex, link):
				link = urlparse.urljoin(seed_url,link)
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)

if __name__ == '__main__':
    link_spider('http://example.webscraping.com', '/(index|view)')