# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    def __init__(self):
        self.author_set = set()

    def process_item(self, item, spider):
        if item['author'] in self.anthor_set:
            raise DropItem("查找到重复姓名的项目：%s"%item )
        else:
            self.author_set.add(item['author'])
        return item


class QidianHotPipeline:
    def process_item(self, item, spider):
        if item["form"] == "连载":
            item["form"] = "LZ"
        else:
            item["form"] = "WJ"
        return item
