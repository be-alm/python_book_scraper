Project: Book Price Web Scraper

Overview:
This Python script automatically scrapes book information from a website and exports the data into a structured CSV dataset. It collects the book title, price, and product link for further analysis.

Features:

- Fetches webpage data automatically
- Extracts book titles
- Extracts book prices
- Collects product page links
- Saves results into a CSV dataset

Technologies:

- Python
- requests
- BeautifulSoup
- pandas

How to run:

python3 src/scrape_books.py

Output:

The script generates a dataset at: data/books.csv

Example dataset fields:

title, price, link