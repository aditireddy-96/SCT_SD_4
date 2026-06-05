import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

names = []
prices = []
ratings = []

books = soup.find_all("article", class_="product_pod")

for book in books:

    name = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    rating = book.p["class"][1]

    names.append(name)
    prices.append(price)
    ratings.append(rating)

data = pd.DataFrame({
    "Product Name": names,
    "Price": prices,
    "Rating": ratings
})

data.to_csv("products.csv", index=False)

print("Data saved to products.csv")