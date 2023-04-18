# Scrapy b_001

## Prerequisites:
```bash
python3 pip -m venv venv
source venv/bin/activate
pip3 install scrapy
scrapy startproject b
scrapy shell
 fetch('https://fsapps.fiscal.treasury.gov/dts/issues')
 response
```


### Links
* [Daily Treasury Statement](https://fsapps.fiscal.treasury.gov/dts/issues)
* [API doc](https://fiscaldata.treasury.gov/api-documentation/#fields-by-endpoint)

### TODO:
1. Download all PDF files
    1. Parse and insert into database (possibly as separate service)
2. Every day download after market closure
    1. Parse and insert into database (possibly as separate service)
3. Suggested: 
	* Write a script that will download all the PDF and sort them by date (It will probably be easier to just stick to the PDF format for all files)
	* Read the files into python and create data frames for each table
	* Clean and structure the data (This will be the most time consuming step)
	* Apply to all PDF
