import scrapy
from work2.items import Work2Item
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass
    
    def parse(self, response):
        pipline_items = []
        # select each movie
        moviess = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        for movie in moviess[:10]:
            list1 = movie.xpath('.//div[contains(@class,"movie-hover-title")]')
            title_selector = list1[0].xpath('./@title')
            title = title_selector.extract_first()
            type_selector = list1[1].xpath('./text()')
            typ = type_selector.extract()[1].strip()
            release_selector = list1[3].xpath('./text()')
            rels= release_selector.extract()[1].strip()
            item = Work2Item()
            item['title'] = title
            item['typ'] = typ
            item['rels'] = rels
            yield item


   