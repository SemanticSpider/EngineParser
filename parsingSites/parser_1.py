import json
import sys
import requests
from bs4 import BeautifulSoup

article = input("Введите артикул товара: ")

url = f"https://www.autoopt.ru/search/index?search={article}"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)

src = req.text

soup = BeautifulSoup(src, "lxml")

products = soup.find_all(
    class_="n-catalog-item relative grid-item n-catalog-item__product"
)

product_j = {}

for product in products:
    product_code = product.find(class_="string bold n-catalog-item__click-copy")
    product_brand = product.find(
        class_="actions brand-popover n-catalog-item__ellipsis"
    )
    product_articul = product.find(
        class_="string bold nowrap n-catalog-item__click-copy n-catalog-item__ellipsis"
    ).text
    product_price = product.find(class_="string nowrap product-list-price__main-price")
    product_count = product.find(class_="fake grass bold mr-0").text
    product_name = product.find(
        class_="n-catalog-item__name-link actions name-popover"
    ).text

    product_j = {
        "Код товара": product_code,
        "Бренд": product_brand,
        "Артикул": product_articul.strip(),
        "Название": product_name.strip(),
        "Цена": product_price,
        "Количество на складе": product_count.strip(),
    }

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(product_j, file, ensure_ascii=False)
