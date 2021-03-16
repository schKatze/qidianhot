#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/3/15
# @Author : 郑煜辉
# @File : qidian_hot_spider
from scrapy import Request
from scrapy.spiders import Spider
from qidian_hot.items import QidianHotItem
from scrapy.loader import ItemLoader


class HotSalesSpider(Spider):
    name = 'hot'
    # start_urls = ["https://www.qidian.com/rank/hotsales?style=1&page=1"]

    # qidian_headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
    # }
    current_page = 1

    def start_requests(self):
        url = "https://www.qidian.com/rank/hotsales?style=1&page=1"
        yield Request(url, callback=self.qidian_parse)

    def qidian_parse(self, response):
        list_selector = response.xpath("// div[@class='book-mid-info']")
        for one_selector in list_selector:
            novel = ItemLoader(item=QidianHotItem(),selector=one_selector)
            novel.add_xpath("name","h4/a/text()")
            novel.add_xpath("author","p[1]/a[1]/text()")
            novel.add_xpath("type","p[1]/a[2]/text()")
            novel.add_css("form",".author span::text")
            # name = one_selector.xpath("h4/a/text()").extract()[0]
            # author = one_selector.xpath("p[1]/a[1]/text()").extract()[0]
            # type = one_selector.xpath("p[1]/a[2]/text()").extract()[0]
            # form = one_selector.xpath('p[1]/span/text()').extract()[0]
            # item = QidianHotItem()
            # item["name"] = name
            # item["author"] = author
            # item["type"] = type
            # item["form"] = form
            yield novel.load_item()

        self.current_page += 1
        if self.current_page <= 5:
            next_url = "https://www.qidian.com/rank/hotsales?style=1&page=%d" % (self.current_page)
            yield Request(next_url,callback=self.qidian_parse)
