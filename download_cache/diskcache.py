# -*- coding:utf-8 -*-
import os
import re
import urlparse
import pickle
from datetime import datetime, timedelta
import zlib

class DiskCache:
	def __init__(self, cache_dir='cache', expires=timedelta(days=30)):		#timedelta将过期时间设置为30天
		self.cache_dir = cache_dir
		self.max_length = max_length
		self.expires = expires
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
				result, timestamp = pickle.loads(zlib.decompress(fp.read()))
				if self.has_expired(timestamp):
					raise KeyError(url + 'has expired')
				return result
		else:
			raise KeyError(url + 'does not exist')

	# 将URL映射为安全文件名,在必要的情况下还需创建父目录
	def __setitem__(self, url, result):
		path = self.url_to_path(url)
		folder = os.path.dirname(path)
		timestamp = datetime.utcnow()
		data = pickle.dumps((result, timestamp))
		if not os.path.exists(folder):
			os.makedirs(folder)
		with open(path, 'wb') as fp:
			fp.write(zlib.compress(data))

	def has_expired(self, timestamp):
		return datetime.utcnow() > timestamp + self.expires



