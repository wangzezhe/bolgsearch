import scrapy
from scrapy.http import Request
from ..items import CrawlsectionItem
from urllib.parse import urljoin
import requests
class CnblogcrawlSpider(scrapy.Spider):
    name = 'cnblogcrawl'
    allowed_domains = ['cnblogs.com']# 注意改为网站对应的一级域名否则会过滤二次解析的域名
    start_urls = ['https://www.cnblogs.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    def parse(self, response, **kwargs):
        article_list = response.xpath('//article[@class="post-item"]')
        item = CrawlsectionItem()
        for article in article_list:
            item['author'] = article.xpath('.//a[@class="post-item-author"]/span/text()').extract_first(),
            item['title'] = article.xpath('.//a[@class="post-item-title"]/text()').extract_first(),
            item['link'] = article.xpath('.//a[@class="post-item-title"]/@href').extract_first(),
            item['delivery_time'] = article.xpath('.//span[@class="post-meta-item"]/span/text()').extract_first()
            yield item

        next_page = response.css('.pager a:contains(">")::attr(href)').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

