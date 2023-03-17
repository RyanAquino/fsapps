import scrapy
import os

from scrapy.http import Request
from pathlib import Path


class FsappsSpider(scrapy.Spider):
    name = "fsapps"
    start_year = 1998
    end_year = 2023
    download_directory_path = Path().cwd() / "data"
    start_urls = [
        f"https://fsapps.fiscal.treasury.gov/dts/issues/{year}" for year in range(start_year, end_year + 1)
    ]

    def __init__(self):
        self.start_urls += self.generate_year_quarter_urls()
        self.download_directory()
        super().__init__()

    def generate_year_quarter_urls(self):
        quarter_per_year = []
        for url in self.start_urls:
            for ctr in range(1, 5):
                quarter_per_year.append(f"{url}/{ctr}")

        return quarter_per_year

    def download_directory(self):
        if not Path(self.download_directory_path).exists():
            os.makedirs(self.download_directory_path)

    def is_file_downloaded(self, filename):
        extensions = ["txt", "xlsx", "pdf"]
        for ext in extensions:
            temp_file_name = f"{filename}.{ext}"
            if (Path(self.download_directory_path) / temp_file_name).exists():
                return True
        return False

    def parse(self, response, **kwargs):
        mapping = {}

        for link in response.css("a::attr(href)"):
            link = link.get()

            if ".txt" in link or "xlsx" in link or ".pdf" in link:
                filename_ext = link.split('/')[-1]
                filename = filename_ext.split(".")[-2]

                if not filename or self.is_file_downloaded(filename):
                    self.logger.warning(f"skipping: {link}")
                    continue

                # Order: xlsx, txt, pdf
                if filename not in mapping:
                    self.logger.info(f"Downloading: {link}")
                    mapping[filename] = response.urljoin(link)

        for item in mapping.values():
            yield Request(
                url=item,
                callback=self.save_pdf
            )

    def save_pdf(self, response):
        filename = response.url.split('/')[-1]
        self.logger.info(f'Saving: {filename}')

        with open(os.path.join(self.download_directory_path, filename), "wb") as f:
            f.write(response.body)
