# SetuCrawler
A web crawler which is used to scratch certain kinds of pictures


# 说明

MyCrawler.py 是原汁原味的爬虫文件，可以将涩图详细内容写入excel表格，便于记录。

但是缺点是需要xlwt模组，部分python用户并没有安装该库，所以会带来一定麻烦

***
Crawler.withoutXLWT.py 是删去XLWT代码部分的爬虫

这样不需要导入xlwt模组也可以直接运行代码，避免了安装麻烦

但是缺点是不能用excel表格记录详细数据

# 更新日志

## 1.0

上传初代涩图爬虫代码，实现爬取pixiv涩图基本功能


## 2.0 

优化代码逻辑，删去不必要代码，更正之前代码中的错误之处、注释中的错误之处


## 3.0

新增搜索功能，可以搜索自己想要的内容

## 3.5

修复3.0版本中的已知BUG，做到流畅运行。

## 4.0

1. 更改库名为CrawlerPackage
2. 上传QQ音乐爬虫（未引入VIP Cookie，目前只能爬取免费音乐）
