# -*- coding:utf-8 -*-
import os
import re
import urlparse
import pickle

class DiskCache:
	def __init__(self, cache_dir='cache'):
		self.cache_dir = cache_dir
		self.max_length = max_length
	# 文件名限制
	def url_to_path(self, url):
		components = urlparse.urlsplit(url)
		path = components.path
		if not path:
			path = '/index/'
		elif path.endswith('/'):
			path += 'index.html'
		filename = components.netloc + path + components.query
		reg = re.sub('[^/0-9a-zA-Z\-.,;_ ]', '_', filename)
		f = '/'.join(segment[:255] for segment in reg.split('/'))
		return os.path.join(self.cache_dir, filename)

	# 首先将URL映射为安全文件名
	def __getitem__(self, url):
		path = self.url_to_path(url)
		if os.path.exists(path):
			with open(path, 'rb') as fp:
				return pickle.load(fp)
		else:
			raise KeyError(url + 'does not exist')

	# 将URL映射为安全文件名,在必要的情况下还需创建父目录
	def __setitem__(self, url, result):
		path = self.url_to_path(url)
		folder = os.path.dirname(path)
		if not os.path.exists(folder):
			os.makedirs(folder)
		with open(path, 'wb') as fp:
			fp.write(pickle.dumps(result))



