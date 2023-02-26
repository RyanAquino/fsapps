import scrapy
import os

from scrapy.http import Request


class FsappsSpider(scrapy.Spider):
    name = "fsapps"
    start_year = 1998
    end_year = 2023
    start_urls = [
        f"https://fsapps.fiscal.treasury.gov/dts/issues/{year}" for year in range(start_year, end_year+1)
    ]

    def __init__(self):
        quarter_per_year = []
        for url in self.start_urls:
            for ctr in range(1, 5):
                quarter_per_year.append(f"{url}/{ctr}")

        self.start_urls += quarter_per_year
        super().__init__()

    def parse(self, response):
        mapping = {}
        for link in response.css("a::attr(href)"):
            link = link.get()

            if ".txt" in link or "xlsx" in link or ".pdf" in link:
                filename = link.split('/')[-1].split(".")[-2]

                if not filename:
                    self.logger.error(f"skipping: {link}")
                    continue

                if ".txt" in link:
                    mapping[filename] = response.urljoin(link)

                if ".xlsx" in link:
                    mapping[filename] = response.urljoin(link)

                if ".pdf" in link:
                    mapping[filename] = response.urljoin(link)

        for item in mapping.values():
            yield Request(
                url=item,
                callback=self.save_pdf
            )

    def save_pdf(self, response):
        filename = response.url.split('/')[-1]
        self.logger.info(f'Saving: {filename}')

        with open(os.path.join(os.getcwd(), "data", filename), "wb") as f:
            f.write(response.body)
