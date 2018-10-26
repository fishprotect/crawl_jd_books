# 主要学习爬取动态加载的页面，用scrapy+splash渲染器

### 爬虫一(quotes)，爬取http://quotes.toscrape.com/js上面的名人名言，
### 爬虫二(jd_book),爬取京东上关于PYTHON的书籍信息，关键词为python。
#### 使用scrapy,splash渲染引擎


## 使用方法
#### 1：$sudo docker run -p 8050:8050 -p 8051:8051 scrapinghub/splash
#### 2: $cd crawl_jd_book_with_splash
#### 3: $用scrapy相应的爬虫

### docker和splash 的安装方法
#### 安装docker:$sudo apt-get install docker
#### 安装splash:$sudo docker pull scraping/splash
