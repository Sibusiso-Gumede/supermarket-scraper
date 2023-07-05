# Supermarket Scraper
A work-in-progress ETL data pipeline. The program scrapes on-promotion product data from multiple supermarket websites, namely Shoprite, PicknPay and more. It then stores the data in binary format for future transformation and loading.

## Table of Contents
- ETL Infrastructure
- Package Managers
- Dependencies
- Project Mockups

## ETL Infrastructure
BeautifulSoup and Playwright library to extract static/dynamic data.    
ConcurrentFutures and AsyncIO library to download multiple images concurrently.  
Pytesserect library to extract data from promotion catalogs.  
PIL and BytesIO library to transform/load data.

## Package Managers
pip (python installation package)

## Dependencies
playwright  
asyncio
