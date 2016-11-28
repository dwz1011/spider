#网络爬虫
###了解网络爬虫

**检查robots.txt**

- 大多数网站都会定义robots.txt，让爬虫了解爬取该网站存在哪些限制

**检查网站地图(sitemap)**

**估算网站大小**

**识别网站所用技术(builtwith)**

> 安装 pip install builtwith

	例：
	>>> import builtwith
	>>> builtwith.parse('http://www.taobao.com/')
	{u'web-servers': [u'Tengine']}
	
**网站所有者(python-whois)**

> 安装 pip install python_whois

	例：
	>>> import whois
	>>> print whois.whois('taobao.com')
	{
	...
	"org": "Zhejiang Taobao Network Limited (\u6d59\u6c5f\u6dd8\u5b9d\u7f51\u7edc\u6709\u9650\u516c\u53f8)",
	  "creation_date": [
	    "2003-04-21 00:00:00",
	    "2003-04-20T20:50:05-0700"
	  ],
	...
	}
	
###开始编写网络爬虫(web_spider)

- **下载网页**
- **网站地图爬虫**
- **ID遍历爬虫**
- **链接爬虫**
- **其他功能**

	> 高级功能(robotparser)
	
		先加载robot.txt文,件通过can_fetch()函数来确定指定的用户代理是否允许访问网页
	
	> 支持代理
	
	> 下载限速
	
	> 避免爬虫陷阱
	
	