import scrapy
import os

from scrapy.http import Request


class FsappsSpider(scrapy.Spider):
    name = "fsapps"
    start_urls = ["https://fsapps.fiscal.treasury.gov/dts/issues"]

    def parse(self, response):
        for link in response.css("a::attr(href)"):
            if ".pdf" in link.get():
                yield Request(
                    url=response.urljoin(link.get()),
                    callback=self.save_pdf
                ) 

    def save_pdf(self, response):
        filename = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', filename)

        with open(os.path.join(os.getcwd(), "data", filename), "wb") as f:
            f.write(response.body)