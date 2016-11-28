# -*- coding:utf-8 -*-
import urllib2
def download(url):
	return urllib2.urlopen(url).read()

if __name__ == '__main__':
	url = 'http://example.webscraping.com'
	print download(url)
