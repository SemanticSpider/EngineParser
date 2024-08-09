import json
import sys
import requests
from time import sleep
from random import uniform
from bs4 import BeautifulSoup


not_robot1 = "https://www.google.com/recaptcha/api2/reload"
not_robot2 = "https://www.google.com/recaptcha/api2/clr"
not_robot3 = "https://autopiter.ru/api/api/not-robot/verification"

data = {"k": "6LeGDIoiAAAAAFLlm8kMJLRzbUJjCbhcW_GXqc5T"}

recaptcha = {'recaptcha': "03AFcWeA59eqnHBi8p89tRn-DAcSQm0PYmJ_wODB4Ip67PF92FJcoqzVFxbt-4kSV5y0awFeOxzjJTdNp9-sfW1644mfQt2UPvPbfcJoWwlOdm8Ql6Irl1KXoKb5sRQJGzLn7x79qbJRzxfvgQQJHv9xU9_LSDons_WXtADsQCM-X3YU_hglmnvE56QpohkqcDdZx0nrmrzEj0b7TICTQ2i2PUdV5yqWul2TuaXpfklz5ctb7BfskNhPWqhufNOzFIzNP5BAjKkrnFGupaHzN7domuC_7BFEdboXYHDJbPoP3Ml3ZV2h3ZNHlfCgsOdW6Td6UtAisPSpB6XhTC4XF7CaKw9SOVX_9OgZwZIgJW-GJOAhnlYencbxlTXHEf_KHXLJ7yWJheAITTIW0-9MVLsJOvvBPJq5S1_nQab6M2khT1iBZTb3c5M5Z-SXnTiumzqcdhRoBTCY5hmqY2LDcLG_PPjLYxbjYoynZEaUK-g021o2v8f_p90L6j9i-MysnepGgnBlDKyVt0WV06UoLFbtfa1jfp5Cu45y5OHEnwgFoQsD9nFGqNyk3ymtGVNs6t9OMvFhIB88lUcLYjrvxYA0k281nhyCNmsU17qSjGNNtY76pmZ105cRo_wiICTsdYTSJH7CAPgmABkMIwjr6DmTs1NKOFc2T03L6NQ2SkEzZXHRvfW-bhjTstiCbsGG8wg00W88CLry0wE7F0O3WBJnq2iUTSF9wFG9NlY1CT-mRTROx5Dv9CWS7Pl01e0RQK9zNddkZDTUdKxrXwvC2_xfp7xPVsQeXjBTtRLHuxsXWvVie7-jifX3vTBraxW0sFdaGaJmKwQVIYXbM-k4ODdBPmt6nl0tE02Q"}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
	"Set-Cookie": "guestId=XOuTXkQ01GTNSUl3c_p3f; Max-Age=2592000;"
}

req_not_robot1 = requests.post(not_robot1, data=json.dumps(data))
req_not_robot2 = requests.post(not_robot2, data=json.dumps(data))
req_not_robot3 = requests.post(not_robot3, data=json.dumps(recaptcha))

print(req_not_robot1)
print(req_not_robot2)
print(req_not_robot3)

proxies = [
"http://qrX2br:0SrrNc@88.218.73.45:9860",
"http://qrX2br:0SrrNc@88.218.75.218:9367",
"http://qrX2br:0SrrNc@88.218.72.250:9833"
]

articles = ["322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010", 
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
			"322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010",
            "322403", "236-1028001", "5360-1118002", "238-1000001-03", "236-1106210-А2", "236-1306054-А", "238-1104001-10", "AVX13-1045LA", "100-3519050", "42021116010"]

article = "322403"


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}


def get_href_product(article):

	url = f"https://autopiter.ru/goods/{article}"

	req = requests.get(url, headers=headers)

	src = req.text
	# print(src)
	soup = BeautifulSoup(src, "lxml")

	product = soup.find("div", "IndividualTableRow__row___111l8")

	product_href = product.find(
		"div", class_="IndividualTableRow__numberColumn___36MQf"
	).find("a", class_="IndividualTableRow__numberLink___1-eq1 common__link___1TmCU").get("href")

	return product_href


product_href = get_href_product(article)


def get_product_info(href):

	url_product = f"https://autopiter.ru{href}"

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
		).find("div").text

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

	return full_product_info


result_object = {}

count = 1

for article in articles:


	href_product = get_href_product(article)

	# sleep_time = uniform(7, 10)
	# sleep(sleep_time)

	product_info = get_product_info(href_product)

	result_object[article] = product_info

	print(f"Complited {count}")

	count += 1

	sleep_time = uniform(20, 25)
	sleep(sleep_time)



with open("data.json", "w", encoding="utf-8") as file:
    json.dump(result_object, file, ensure_ascii=False)
