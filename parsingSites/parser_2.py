import json
import sys
import requests
from bs4 import BeautifulSoup

# получение артикула товара
article = input("Введите артикул товара: ")

# формирование url для запроса на сайт
url = f"https://autopiter.ru/goods/{article}"

# передача заголовков в запрос
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)

src = req.text

soup = BeautifulSoup(src, "lxml")

products = soup.find_all(class_="IndividualTableRow__row___111l8")

product_j = {}

for product in products:
    # product_code = product.find(class_="string bold n-catalog-item__click-copy").text
    product_brand = product.find(
        class_="ModalButton__button___3fjTP new-common__unstyledButton___zigzA"
    ).text
    product_articul = product.find(
        class_="IndividualTableRow__numberLink___1-eq1 common__link___1TmCU"
    ).text
    # product_price = product.find(class_="string nowrap product-list-price__main-price")
    product_count = product.find(class_="IndividualTableRow__emptyStock___2dtEt")
    product_name = product.find(
        class_="IndividualTableRow__descriptionColumn___dFBnQ"
    ).text

    product_j = {
        "Бренд": product_brand.strip(),
        "Артикул": product_articul.strip(),
        "Название": product_name.strip(),
        "Количество на складе": product_count,
    }

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(product_j, file, ensure_ascii=False)
