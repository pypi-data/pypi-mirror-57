# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['stand']

package_data = \
{'': ['*']}

install_requires = \
['Scrapy==1.8.0', 'fake-useragent==0.1.11', 'peewee==3.12.0', 'schedule==0.6.0']

entry_points = \
{'console_scripts': ['stand = stand.main:run']}

setup_kwargs = {
    'name': 'stand',
    'version': '0.1.11',
    'description': 'IP代理池',
    'long_description': '# IP 代理池\n\n## 安装\n\n```sh\npip install stand\n```\n\n## 启动\n\n```sh\nstand\n```\n\n## 使用\n\n```python\n>>> from stand import get_proxy\n>>> proxy = get_proxy()\n>>> print(proxy)\n\'103.133.222.151:8080\'\n```\n\n在 Scrapy 中使用 stand 作为代理\n\n```python\nimport scrapy\nfrom scrapy.crawler import CrawlerProcess\n\n\nclass TestSpider(scrapy.Spider):\n    name = \'test\'\n    start_urls = [\'https://api.ip.sb/ip\']\n\n    def parse(self, response):\n        print(response.meta[\'proxy\'])\n        print(response.text)\n\n\nDOWNLOADER_MIDDLEWARES = {\n    \'stand.UserAgentMiddleware\': 543,\n    \'stand.ProxyMiddleware\': 600,\n}\nsettings = dict(\n    LOG_ENABLED=False,\n    DOWNLOAD_TIMEOUT=30,\n    DOWNLOADER_MIDDLEWARES=DOWNLOADER_MIDDLEWARES,\n)\n\n\ndef run():\n    process = CrawlerProcess(settings)\n    process.crawl(TestSpider)\n    process.start()\n\n\nif __name__ == "__main__":\n    run()\n```\n\n## 项目说明\n\n1. 当启动 `stand` 时, 首先会运行 `crawl` 函数从代理网站爬取代理 IP, 并将爬取到的结果存储在名为 stand.db (可通过 `STAND_DIR` 环境变量设置保存目录) 的 SQLite 数据库中, 每个 IP 有一个初始分数 2\n2. 然后会运行 `validate` 函数验证代理 IP 的有效性, 验证通过分数设置为最高值 3, 验证失败分数减 1, 当分数为 0 时删除该 IP\n3. 之后会定时运行 `crawl` 和 `validate` 函数分别爬取和验证 IP, 每20分钟爬取一次 IP, 每60分钟验证一次 IP\n',
    'author': 'lin-zone',
    'author_email': 'z_one10@163.com',
    'url': 'https://github.com/lin-zone/stand',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
