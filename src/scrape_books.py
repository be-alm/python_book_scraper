import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code != 200:
    print(f"Failed to fetch page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

books = []

articles = soup.find_all("article", class_="product_pod")

books = []

articles = soup.find_all("article", class_="product_pod")

for article in articles:
    title = article.h3.a["title"]
    price = article.find("p", class_="price_color").text
    link = "http://books.toscrape.com/catalogue/" + article.h3.a["href"]

    books.append({
        "title": title,
        "price": price,
        "link": link
    })

df = pd.DataFrame(books)
df.to_csv("data/books.csv", index=False)

print("Scraping complete. Data saved to data/books.csv")