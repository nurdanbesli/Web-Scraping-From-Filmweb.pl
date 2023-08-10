import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://www.filmweb.pl/']
    start_urls = ['https://www.filmweb.pl/ranking/film?fbclid=IwAR0qC8KuR4Z159TFqObUBnv3jETlH6yKX7tgtovXJqxrMRs3bG0veCpA4wQ']

    def parse(self, response):
        xpath = '//h2[@class="rankingType__title"]/a/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.filmweb.pl' + s.get()
            yield l

    def start_requests(self):
        url = "https://www.filmweb.pl/ranking/film"
        pages = 5  # Change the number of pages you want to scrape

        for page in range(1, pages + 1):
            page_url = f"{url}?page={page}"
            yield scrapy.Request(page_url, callback=self.parse)

class Film(scrapy.Item):
    movie_name = scrapy.Field()
    publication_year = scrapy.Field()
    duration = scrapy.Field()
    ranking = scrapy.Field()
    genre = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'films'
    allowed_domains = ['www.filmweb.pl']

    def start_requests(self):
        with open("C:/Users/nurdanbesli/Desktop/Scrapy/links.csv", "rt") as f:
            for url in f.readlines()[1:]:
                yield scrapy.Request(url.strip(), callback=self.parse)

    def parse(self, response):
        f = Film()

        f['movie_name'] = response.xpath('//div[@class="filmCoverSection__titleDetails"]//h1[contains(@class, "filmCoverSection__title")]/text()').get()
        f['publication_year'] = response.xpath('//div[@class="filmCoverSection__year"]/text()').get()
        f['duration'] = response.xpath('//div[@class="filmCoverSection__duration" and @itemprop="timeRequired"]/text()').get()
        f['ranking'] = response.xpath('//span[@class="filmRating__rateValue"]/text()').get()
        f['genre'] = response.xpath('//div[@class="filmInfo__info" and @itemprop="genre"]/span/a/text()').getall()

        yield f