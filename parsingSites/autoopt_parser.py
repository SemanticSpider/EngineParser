import json
import sys
import requests
from time import sleep
from random import uniform
from bs4 import BeautifulSoup

articles = ["322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010", 
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
			"322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010"]

article = "3302-1602408"

url = f"https://www.autoopt.ru/search/index?search={article}"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

def get_product_info(article=article):

    url = f"https://www.autoopt.ru/search/index?search={article}"

    req = requests.get(url, headers=headers)

    src = req.text

    result_mas = []

    soup = BeautifulSoup(src, "lxml")

    all_products = soup.find_all(
        "div", class_="n-catalog-item relative grid-item n-catalog-item__product"
    )

    for product in all_products:

        # получение кода товара
        product_code = product.find(
            "div", class_="n-catalog-item__photo-code"
        ).find(
            "span", class_="string bold n-catalog-item__click-copy n-catalog-item__ellipsis"
        ).text

        # получение названия бренда товара
        product_brand = product.find(
            "div", class_="n-catalog-item__brand d-none d-md-table-cell"
        ).find(
            class_="n-catalog-item__ellipsis"
        ).text.strip()

        # получение артикула товара
        product_article = product.find(
            "div", class_="n-catalog-item__article"
        ).find(
            "span", class_="n-catalog-item__ellipsis"
        ).text

        # получение названия товара
        product_name = product.find(
            "div", class_="string"
        ).find(
            "a", class_="n-catalog-item__name-link"
        ).text.strip()

        # получение цен товара
        if product.find("div", class_="n-catalog-item__price-box col-12 col-md pr-0 mb-2") == None:
            pass
        else:

            product_prices = product.find(
                "div", class_="n-catalog-item__price-box col-12 col-md pr-0 mb-2"
            ).find(
                "ul"
            ).find_all(
                "li"
            )

            product_price_obj = {}

            for price in product_prices:
                type_price = price.find(
                    class_="fake mr-2 link-color price5").text.strip()
                cur_price = price.find(class_="gray").text
                product_price_obj[type_price] = cur_price

        # получение количества товаров
        count = product.find(
            "span", class_="fake grass bold mr-0"
        )

        if count != None:
            product_count = product.find(
                "div", class_="n-catalog-item__count-box"
            ).find(
                "span", class_="fake grass bold mr-0"
            ).text.strip()[:-1]
            product_count = int(product_count)
        else:
            count = product.find(
                "span", class_="fake link-gray"
            )
            if count != None:
                product_count = count.text
            else:
                product_count = product.find(
                    "offers"
                ).get(":offers")
                product_count = json.loads(product_count)[0]["quantity"]

        result_mas.append(
            {
                "Код товара": product_code,
                "Бренд товара": product_brand,
                "Артикул товара": product_article,
                "Цены товара": product_price_obj,
                "Количество на складе": product_count,
            }
        )
    
    return result_mas


result_object = {}

count = 1

for article in articles:

	product_info = get_product_info(article)

	result_object[count] = product_info

	print(f"Complited {count}")

	count += 1

	sleep_time = uniform(5, 7)
	sleep(sleep_time)


with open("data.json", "w", encoding="utf-8") as file:
    json.dump(result_object, file, ensure_ascii=False)
