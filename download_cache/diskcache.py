# -*- coding:utf-8 -*-
import os
import re
import urlparse

class DiskCache:
	def __init__(self, cache_dir='cache'):
		self.cache_dir = cache_dir
		self.max_length = max_length
	def url_to_path(self, url):
		components = urlparse.urlsplit(url)
		path = components.path
		if not path:
			path = '/index/'
		elif path.endswith('/')
			path += 'index.html'
		filename = components.netloc + path + components.query
		reg = re.sub('[^/0-9a-zA-Z\-.,;_ ]', '_', filename)
		f = '/'.join(segment[:255] for segment in reg.split('/'))
		return os.path.join(self.cache_dir, filename)

		
