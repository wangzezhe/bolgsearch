# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from .models.es_type import ArticleType
from scrapy.exporters import JsonLinesItemExporter
class CrawlsectionPipeline(object):
    def __init__(self):
        self.fp = open('store.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def spider_start(self,spider):
        print("爬虫开始")

    def process_item(self, item, spider):
        article = ArticleType()
        article.title = item['title']
        article.link = item['link']
        article.author = item['author']
        article.delivery_time = item['delivery_time']
        article.save()
        self.exporter.export_item(item)
        return item

    def spider_end(self,spider):
         self.fp.close()
         print('爬虫结束')