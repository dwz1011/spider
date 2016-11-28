# -*- coding: utf-8 -*-

import urllib2
import re

def spider(html):
	reg = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)[0]
	return reg

if __name__ == '__main__':
	url = 'http://example.webscraping.com/view/United-Kingdom-239'
	html = urllib2.urlopen(url).read()
	print spider(html)