import scrapy
import os

from scrapy.http import Request


class FsappsSpider(scrapy.Spider):
    name = "fsapps"
    year = 2023
    start_urls = [
        f"https://fsapps.fiscal.treasury.gov/dts/issues/{year}" for year in range(1998, year+1)
    ]

    def __init__(self):
        quarter_per_year = []
        for url in self.start_urls:
            for ctr in range(1, 5):
                quarter_per_year.append(f"{url}/{ctr}")

        self.start_urls += quarter_per_year
        super().__init__()

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
