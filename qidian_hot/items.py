# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


def form_convert(form):
    if form[0] == "连载":
        return "LZ"
    else:
        return "WJ"


class QidianHotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    author = scrapy.Field(output_processor=TakeFirst())
    type = scrapy.Field(output_processor=TakeFirst())
    form = scrapy.Field(input_processor=form_convert, output_processor=TakeFirst())
