import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# SET YOUR PRODUCT HERE
product = "Samsung Galaxy M14"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Flipkart Search URL
search_url = f"https://www.flipkart.com/search?q={product.replace(' ', '+')}"

response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

try:
    product_block = soup.find("div", {"class": "_1AtVbE"})  # first product block
    name = product_block.find("div", {"class": "_4rR01T"}).text.strip()
    price = product_block.find("div", {"class": "_30jeq3 _1_WHN1"}).text.strip()
    availability = "Available"
except:
    name = product
    price = "N/A"
    availability = "Not Found"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save to CSV
data = {
    "Timestamp": [timestamp],
    "Product": [name],
    "Price": [price],
    "Availability": [availability]
}

df = pd.DataFrame(data)

# Append to file
try:
    df.to_csv("price_history.csv", mode='a', header=not pd.io.common.file_exists("price_history.csv"), index=False)
except:
    df.to_csv("price_history.csv", index=False)

print("✅ Price data saved:", name, price, availability)
