import scrapy
from ..items import AmazonItem
from urllib import parse
from scrapy.utils.response import open_in_browser

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.koovs.com/tags/sweet-summer-vibes?type=list&sort=relevance&filter_category_fq=664']

    def parse(self, response):
        item = AmazonItem()
        products = response.css('div.a-section.a-spacing-medium')
        # asin = []
        # title = response.css('.a-size-base-plus.a-text-normal::text').extract()
        # price = response.css('span.a-offscreen').css('::text').extract()
        # image = response.css('.s-image::attr(src)').extract()
        # urls = response.css('.a-size-base.a-link-normal.a-text-normal::attr(href)').extract()
        # for url in urls:
        #     url = url.split("dp")[-1]
        #     if(url[0]=='%'):
        #         asin.append(url[3:13])
        #     elif(url[0]=='/'):
        #         asin.append(url[1:11])
        # for x in range(0,len(title)):
        #     item = AmazonItem()
        #     item['no'] = x
        #     item['title'] = title[x]
        #     item['asin'] = asin[x]
        #     item['price'] = price[x]
        #     item['image'] = image[x]
        #     yield item
        a=1
        for x in products:
            item['no'] = a
            a = a+1
            title = x.css('.a-size-base-plus.a-text-normal::text').extract()
            pricew = x.css('.a-price-whole::text').extract()
            pricef = x.css('.a-price-fraction::text').extract()
            image = x.css('.s-image::attr(src)').extract()
            url = x.css('.a-size-base.a-link-normal.a-text-normal::attr(href)').extract()
            url = str(url)
            url = url.split("dp")[-1]
            if(url[0]=='%'):
                item['asin']=(url[3:13])
            elif(url[0]=='/'):
                item['asin']=(url[1:11])
            item['title'] = ''.join(title)
            pw = ''.join(pricew)
            pf = ''.join(pricef)
            item['price'] = pw+pf
            item['image'] = ''.join(image)
            # print(title[0])
            yield item
        open_in_browser(response)
        # print('title 0:'+title[0])
        # yield item
        # for url in urls:
            # url = parse.urljoin(response.url, url)
        #     yield scrapy.http.Request(url, callback=self.parse_page)
        # view(response)
        # print('length: '+str(len(items['title'])))


    # def parse_page(self, response):
    #     asin = response.css('#productDetails_detailBullets_sections1 tr:nth-child(4) .a-size-base').css('::text').extract()
    #     print(asin)
        # title = response.css('[class="posting-headline"]
        #     h2::text').extract()
        # text = response.css('[class="section page-centered"]
        #     div::text').extract()[1]
        # scraped_info = {
        #     'title' : title,
        #     'text' : text
        #             }
