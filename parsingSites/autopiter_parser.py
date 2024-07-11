import json
import sys
import requests
from bs4 import BeautifulSoup

article = "162622"

url = f"https://autopiter.ru/goods/{article}"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)

src = req.text

soup = BeautifulSoup(src, "lxml")

product = soup.find("div", "IndividualTableRow__row___111l8")

product_brand = product.find(
    "div", class_="IndividualTableRow__infoColumn___1HOcm"
).find(
    "span", class_="ModalButton__button___3fjTP new-common__unstyledButton___zigzA"
).find("span").text

product_article = product.find(
    "div", class_="IndividualTableRow__numberColumn___36MQf"
).find("a", class_="IndividualTableRow__numberLink___1-eq1 common__link___1TmCU").text

product_name = product.find(
    "div", class_="IndividualTableRow__descriptionColumn___dFBnQ"
).text

product_href = product.find(
    "div", class_="IndividualTableRow__numberColumn___36MQf"
).find("a", class_="IndividualTableRow__numberLink___1-eq1 common__link___1TmCU").get("href")

url_product = f"https://autopiter.ru{product_href}"

req_product = requests.get(url_product, headers=headers)

src_product = req_product.text

soup_product = BeautifulSoup(src_product, "lxml")

# print(soup_product.text)
# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(json.loads(soup_product), file, ensure_ascii=False)
