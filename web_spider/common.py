# -*- coding:utf-8 -*-
import urllib2

def download(url):
	print 'downloading:', url
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Downloading error:', e.reason
		html = none
	return html


if __name__ == '__main__':
	url = 'http://example.webscraping.com'
	print download(url)
