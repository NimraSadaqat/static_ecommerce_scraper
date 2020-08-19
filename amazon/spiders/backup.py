import scrapy
from ..items import AmazonItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.amazon.com/s?k=garlic+press&ref=nb_sb_noss_2']

    def parse(self, response):
        items = AmazonItem()
        title = response.css('.a-color-base.a-text-normal::text').extract()
        author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        price = response.css('.a-price span').css('::text').extract()
        image = response.css('.s-image::attr(src)').extract()

        items['title'] = title
        items['author'] = author
        items['price'] = price
        items['image'] = image
        yield items
