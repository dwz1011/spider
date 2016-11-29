# -*- coding:utf-8 -*-

import urllib2
import re
import urlparse
import robotparser
from datetime import datetime
import Queue
from downloader import Downloader

def normalize(seed_url, link):
    link, _ = urlparse.urldefrag(link) 
    return urlparse.urljoin(seed_url, link)

def same_domain(url1, url2):
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc

def get_links(html):
	reg = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	return reg.findall(html)


def get_robots(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp

def link_spider(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp', proxy=None, num_retries=1):
    crawl_queue = Queue.deque([seed_url])
    seen = {seed_url: 0}
    num_urls = 0
    rp = get_robots(seed_url)
    throttle = Throttle(delay)
    D = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, num_retries=num_retries, cache=cache)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent
    while crawl_queue:
        url = crawl_queue.pop()
        depth = seen[url]
        if rp.can_fetch(user_agent, url):
            throttle.wait(url)
            html = D(url)
            links = []
            if depth != max_depth:
                if link_regex:
                    links.extend(link for link in get_links(html) if re.match(link_regex, link))
                for link in links:
                    link = normalize(seed_url, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        if same_domain(seed_url, link):
                            crawl_queue.append(link)
            num_urls += 1
            if num_urls == max_urls:
                break
        else:
            print 'Blocked by robots.txt:', url

if __name__ == '__main__':
    link_spider('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')