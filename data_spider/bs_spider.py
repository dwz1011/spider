# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

def bs_spider(html):
    soup = BeautifulSoup(html, 'lxml') 
    tr = soup.find(attrs={'id':'places_area__row'}) 
    td = tr.find(attrs={'class':'w2p_fw'}) 
    area = td.text 
    return area

if __name__ == '__main__':
	url = 'http://example.webscraping.com/view/United-Kingdom-239'
	html = urllib2.urlopen(url).read()
	print bs_spider(html)