# -*- coding:utf-8 -*-

from common import *
import itertools

def iteration_spider():
	for page in itertools.count(1):
		url = 'http://example.webscraping.com/view/- %d' % page
		html = download(url)
		if html is None:
			break
		else:
			pass

if __name__ == '__main__':
	iteration_spider()