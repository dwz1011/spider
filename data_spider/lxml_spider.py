# -*- coding: utf-8 -*-

import urllib2
import lxml.html

def spider(html):
	tree = lxml.html.fromstring(html)
	td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
	area = td.text_content()
	return area

if __name__ == '__main__':
	url = 'http://example.webscraping.com/view/United-Kingdom-239'
	html = urllib2.urlopen(url).read()
	print spider(html)