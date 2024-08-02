import json
import sys
import requests
from bs4 import BeautifulSoup

article = "476Q1002901"

url = f"https://autopiter.ru/goods/{article}"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)

src = req.text

soup = BeautifulSoup(src, "lxml")

product = soup.find("div", "IndividualTableRow__row___111l8")

product_href = product.find(
    "div", class_="IndividualTableRow__numberColumn___36MQf"
).find("a", class_="IndividualTableRow__numberLink___1-eq1 common__link___1TmCU").get("href")

# print(product_href)

url_product = f"https://autopiter.ru{product_href}"

req_product = requests.get(url_product, headers=headers)

src_product = req_product.text

soup_product = BeautifulSoup(src_product, "lxml")

products_information = soup_product.find(
	"table", class_="NonRetailAppraiseTable__table___7gnpi"
).find("tbody").find_all(
	"tr", class_="NonRetailAppraiseTR__tr___3rq83"
)

full_product_info = []

for product_info in products_information:
	
	# Получение региона продукта
	product_region = product_info.find(
		"div", class_="NonRetailAppraiseTR__regionInner___3FAjj"
	).text

	# Получение бренда продукта
	product_brand = product_info.find(
		"span", class_="NonRetailAppraiseTR__brandLink___v2r3Y ModalButton__root___pxLdy"
	).find(
		"span", class_="ModalButton__button___3fjTP new-common__unstyledButton___zigzA"
	).text

	# Получение артикула продукта
	product_article = product_info.find_all("td")[2].text

	# Получение имени продукта
	product_name = product_info.find(
		"td", class_="NonRetailAppraiseTR__nameCell___2k4_I"
	).find("div", class_="NonRetailAppraiseTR__nameCellInner___sPiuJ").text

	# Получение количетсва продукта
	product_count = product_info.find(
		"td", class_="NonRetailAppraiseTR__quantityCell___nzLgM"
	).find(
		"div", class_="NonRetailAppraiseTR__quantity___18gVh"
	).text

	# Получение информации через сколько придет продукт
	product_time = product_info.find(
		"td", class_="NonRetailAppraiseTR__daysCell___YR7jI"
	).find("span", "NonRetailAppraiseTR__days___UfW_V").text

	# Получение стоимости продукта
	product_price = product_info.find(
		"td", "NonRetailAppraiseTR__priceCell___2hvw7"
	).find("div", "NonRetailAppraiseTR__priceWrapper___2sj3p").text


	full_product_info.append(
        {
            "Регион поставщика": product_region,
            "Производитель": product_brand,
            "Номер": product_article,
            "Наименование": product_name,
            "Наличие, шт": product_count,
            "Срок (дн)": product_time,
            "Цена": product_price,
        }
    )

print(full_product_info)


# print(soup_product.text)
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(full_product_info, file, ensure_ascii=False)
