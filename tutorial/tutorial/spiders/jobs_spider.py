import scrapy


class QuotesSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
            'https://www.carmera.com/join/',
            'https://www.betterment.com/careers/current-openings/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'site-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
