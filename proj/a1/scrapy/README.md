# Scrapy-app

Scrapy-app is an project that can scrape the PDF links on a website and download it.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```


## Navigate to project
```bash
cd proj/scrapy
```

Scrapy is the module used on this project. More info can be found on this [Documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html).

## Usage

Run the following command on the CLI
```python
scrapy crawl fsapps
```

Run with log file as output
```python
scrapy crawl fsapps --logfile=fsgov.log
```


## Running parsers on scraped files
### Navigate to fsapps package
```bash
cd proj/scrapy/fsapps
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run parser for desired file type
Text parser
```python
python text_parser.py
```

Excel parser
```python
python xlsx_parser.py
```

PDF Parser
```python
python pdf_parser.py
```
