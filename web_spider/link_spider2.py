# -*- coding:utf-8 -*-

import urllib2
import re
import urlparse
import robotparser
from datetime import datetime

def get_links(html):
	reg = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	return reg.findall(html)

def download(url, num_retries=2, proxy=None, user_agent='wswp'):
	print 'downloading:', url
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)
	opener = urllib2.build_opener()
	if proxy:
		proxy_params = {urlparse.urlparse(url).scheme: proxy}
		opener.add_handler(urllib2.ProxyHandler(proxy_params))
	try:
		html = opener.open(request).read()
	except urllib2.URLError as e:
		print 'Downloading error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code <= 600:
				return download(url, num_retries-1, proxy, user_agent)
	return html

class Throttle:
	"""docstring for Throttle"""
	def __init__(self, delay):
		self.delay = delay
		self.domains = {}

	def wait(self, url):
		domain = urlparse.urlparse(url).netloc
		last_accessed = self.domains.get(domain)
		if self.delay > 0 and last_accessed is not None:
			sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
			if sleep_secs > 0:
				time.sleep(sleep_secs)
		self.domains[domain] = datetime.now()
		
def link_spider(seed_url, link_regex, delay=0):
	crawl_queue = [seed_url]
	seen = set(crawl_queue)
	rp = robotparser.RobotFileParser()
	throttle = Throttle(delay)
	rp.set_url(urlparse.urljoin(seed_url, '/rocot.txt'))
	rp.read()
	user_agent = 'GoodCrawler'
	while crawl_queue:
		url = crawl_queue.pop()
		if rp.can_fetch(user_agent, seed_url):
			throttle.wait(url)
			html = download(url)
			for link in get_links(html):
				if re.match(link_regex, link):
					link = urlparse.urljoin(seed_url,link)
					if link not in seen:
						seen.add(link)
						crawl_queue.append(link)
		else:
			print 'Blocked by robots.txt', url

if __name__ == '__main__':
    link_spider('http://example.webscraping.com', '/(index|view)')