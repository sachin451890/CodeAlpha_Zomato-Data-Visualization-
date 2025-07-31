import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for page in range(2, 12):
    url = f"https://www.flipkart.com/search?q=mobile+under+50000&page={page}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    product_boxes = soup.find_all("div", class_="DOjaWF gdgoEp")

    for box in product_boxes:
        # Product Name
        name_tag = box.find("div", class_="KzDlHZ")
        Product_name.append(name_tag.text if name_tag else "N/A")

        # Price
        price_tag = box.find("div", class_="Nx9bqj _4b5DiR")
        Prices.append(price_tag.text if price_tag else "N/A")

        # Description
        desc_tag = box.find("ul", class_="G4BRas")
        Description.append(desc_tag.text if desc_tag else "N/A")

        # Review
        review_tag = box.find("div", class_="XQDdHH")
        Reviews.append(review_tag.text if review_tag else "N/A")

# Ensure equal lengths
min_len = min(len(Product_name), len(Prices), len(Description), len(Reviews))
df = pd.DataFrame({
    "Product Name": Product_name[:min_len],
    "Prices": Prices[:min_len],
    "Description": Description[:min_len],
    "Reviews": Reviews[:min_len]
})

df.to_csv("Flipkart_mobile_under_50000.csv", index=False)
