from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivymd.uix.button import MDButton
from plyer import filechooser
import os
import pandas as pd
import openpyxl as op
from openpyxl import load_workbook
import re
import json
import sys
import requests
from time import sleep
from random import uniform
from bs4 import BeautifulSoup
from random import randint

class LoadCard(MDCard):

    loadFile = StringProperty()
    label = StringProperty()
    cardColor = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5
        Window.bind(on_drop_file=self.selectFile)
        
    # Метод, вызываемый при нажатии на кнопку загрузки файла
    def changeFile(self):        
        # Выбор фалйа в filechooser
        choose = filechooser.open_file(on_selection=self.selectFile)

    # Обработчик события выбора файла в filechooser, записывает путь к выбранному файлу в поле loadFile
    def selectFile(self, *args):
        # Получаем путь к файлу
        if(type(args[0]) == list):
            # Из filechooser
            self.loadFile = args[0][0] if len(args[0]) != 0 else self.loadFile
        else:
            # Из Drag-n-Drop
            self.loadFile = args[1].decode(encoding="utf-8")
        
        # Осуществляем проверку Excel расширения
        if self.loadFile and self.loadFile.endswith((".xls", ".xlt", ".xlsx", ".xlsm", ".xltx", ".xltm")):
            self.cardColor = [0.0, 0.5019607843137255, 0.0, 0.3]
            self.label = "Файл {} загружен!".format(self.loadFile.split('\\').pop())
        elif self.loadFile == "":
            pass        
        else: 
            self.cardColor = [1.0, 0.0, 0.0, 0.5]
            self.label = "Принимаются только файлы excel!"
            self.loadFile = ""

    # Ограничиваем дефолтное поведение карточки, чтобы убрать автоматическое изменение цвета
    def set_properties_widget(self):
        super().set_properties_widget()
        self.md_bg_color = self.cardColor
        return True
    
class LoadDirectory(MDBoxLayout):

    savePath = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open(os.path.dirname(os.path.realpath(__file__)) + "\\loadDirectory.txt", "a+") as loadDir:
            loadDir.seek(0, 0)
            self.savePath = loadDir.read()
    
    def chooseDirectory(self):

        def selectDirectory(selectedDirectory):
            self.savePath = selectedDirectory = selectedDirectory[0] if(len(selectedDirectory)) != 0 else self.savePath
            with open(os.path.dirname(os.path.realpath(__file__)) + "\\loadDirectory.txt", "w") as loadDir:
                loadDir.write(self.savePath)

        directory = filechooser.choose_dir(on_selection=selectDirectory)

class LaunchButton(MDButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Класс окна
class Root(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class EngineParser(MDApp):

    # Дефолтные настройки приложения
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.maximize()
 
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.screen = Root()

        loadCard = LoadCard(loadFile = "", label="Загрузите файл", cardColor=self.theme_cls.backgroundColor)        
        loadDirectory = LoadDirectory()
        launchButton = LaunchButton()

        self.screen.add_widget(loadCard)
        self.screen.add_widget(loadDirectory)
        self.screen.add_widget(launchButton)
        # print([widget for widget in self.screen.children if widget.name == "LoadCard"][0].buttonText)
        return self.screen
    
    def launchParse(self, **kwargs):
        properties = {widget.name: widget for widget in self.screen.children if widget.name in ["LoadCard", "LoadDirectory"]}
        loadFile, savePath = [properties["LoadCard"].loadFile, properties["LoadDirectory"].savePath]
        goodsExcelInfo = self.excelFormat(loadFile)
        self.searchBenefit(goodsExcelInfo)



    
    def excelFormat(self, excelFile):
        # Читаем с openpyxl
        wb = load_workbook(excelFile, data_only=True)
        sheet = wb.active

        df = pd.DataFrame(sheet.values)

        artikulMas, name, col, price, cost = [pd.Series()]*5

        dataDeletePattern = re.compile(r"(?:(?<=[ ])\d{2}[\.-]\d{2}[\.-]\d{4}\b)|(?:(?<=[ ])\d{4}[\.-]\d{2}[\.-]\d{2}[ :-]?(?:\d{2}[ :]\d{2}[ :]\d{2})?\b)|(?:(?<=[ ])\b(?:\d{2}[\.-]){2}[А-ЯA-Z]+\b)")
        # artikulSearch = re.compile(r"(?:\b(?:\d+[ ])+\d+\b)|(?:\b[A-Z]+[\. -]?(?:\d+[\.-]?)+\b)|(?:\b(?<![\.,])(?<!ГОСТ )(?:[A-ZА-Я\d]+[\.-])+[A-ZА-Я\d]+\b)|(?:\b\d+[A-ZА-Я]+\d+\b)|(?:\b(?<!ГОСТ )\d{5,}[A-ZА-Я]+\b)|(?:\b(?<!ГОСТ )\d{7,}\b)|(?:\b(?:[A-ZА-Я]\([A-ZА-Я]\)-\d+)\b)")
        artikulSearch = re.compile(r"(?:\b(?<![\.,])(?<!ГОСТ )(?:[A-ZА-Я\d]+[\.-])+[A-ZА-Я\d]+\b)|(?:\b(?:\d+[ ])+\d+\b)|(?:\b[A-Z]+[\. -]?(?:\d+[\.-]?)+\b)|(?:\b\d+[A-ZА-Я]+\d+\b)|(?:\b(?<!ГОСТ )\d{5,}[A-ZА-Я]+\b)|(?:\b(?<!ГОСТ )\d{7,}\b)|(?:\b(?:[A-ZА-Я]\([A-ZА-Я]\)-\d+)\b)")
        

        while(df.iloc[0].isna().sum() == df.iloc[0].size):
            df = df.drop(df.index[0])
        for index, column in df.items():
            if(column.isna().sum() == column.size): 
                df = df.drop(index, axis=1)
                continue

            if(column.astype(str).str.contains(dataDeletePattern).any()): 
                df[index], column = [column.astype(str).str.replace(dataDeletePattern, "", regex=True)]*2

            if(column.astype(str).str.contains(r"(?:[Аа]ртикул)|(?:[Кк]аталожный номер)").any()): artikulMas = column.dropna()

            # if(column.astype(str).str.contains(r"(?:[Аа]ртикул)|(?:[Кк]аталожный номер)").any()): artikulMas = artikulMas.combine(column, lambda s1, s2: s1 if s2 == None else s2).dropna()
            # elif(column.astype(str).str.contains(artikulSearch).any()):
            #     artikulMas = column.dropna() if artikulMas.empty else artikulMas.combine(column, lambda s1, s2: s2 if s1 == None else s1).dropna()

            # if(column.astype(str).str.contains(artikulSearch).any()): artikulMas = artikulMas.combine_first(column.dropna())
            # if(column.astype(str).str.contains(r"(?<!\d{2}.)\d{2,}[\.-]\d{3,}(([\.-]\d+)+)?").any()): artikulMas.append(column.dropna())
            if(column.astype(str).str.contains(r"(?:[Нн]аименование)|(?:ТМЦ)").any()): name = column.dropna()
            elif(column.astype(str).str.contains(r"[Кк]ол-во").any()): col = column.dropna()
            elif(column.astype(str).str.contains(r"[Цц]ена").any()): price = column.dropna()
            elif(column.astype(str).str.contains(r"(?:[Сс]тоимость)|([Сс]умма)").any()): cost = column.dropna()
            
        resultObject = {
            "goods": [],
            "errors": []
        }  

        for index, goodsName in name.items():
            if index in artikulMas.index:
                print(artikulMas.loc[index], " => ", re.search(artikulSearch, str(artikulMas.loc[index])))
                search = re.split(r"/", str(artikulMas.loc[index])) if re.search(artikulSearch, str(artikulMas.loc[index])) else []
            else:
                search = re.findall(artikulSearch, str(goodsName))
                
            if len(search) != 0:
                mainArtikul = search[0]
                if len(search) > 1:
                    for artikul in search:
                        if len(re.sub(r"[ \.-]", "", artikul)) > len(re.sub(r"[ \.-]", "", mainArtikul)): mainArtikul = artikul
                resultObject["goods"].append({
                    "mainArtikul": mainArtikul,
                    "artikuls": search,
                    "name": name.loc[index] if not name.empty and index in name.index else None,
                    "amount": col.loc[index] if not col.empty and index in name.index else None,
                    "price": price.loc[index] if not price.empty and index in name.index else None,
                    "cost": cost.loc[index] if not cost.empty and index in name.index else None,
                })
            else: resultObject["errors"].append(goodsName)
        return resultObject
    
    def get_product_info(self, article):

        url = f"https://www.autoopt.ru/search/index?search={article}"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }

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


            # получение цен товара с разными днями доставки
            if product.find("offers") == None:
                pass
            else:
                product_prices = product.find(
                    "offers")
                # print(json.loads(product_prices[":offers"])[0])              
                product_price_obj = [{"Цена": product["price"], "Количество": product["quantity"], "Доставка": product["deliveryDate"]} for product in json.loads(product_prices[":offers"])]
            
            # получение цен товара
            if product.find("div", class_="n-catalog-item__price-box col-12 col-md pr-0 mb-2") == None:
                pass
            else:
                product_price_obj = {}
                product_prices = product.find(
                    "div", class_="n-catalog-item__price-box col-12 col-md pr-0 mb-2"
                ).find(
                    "ul"
                ).find_all(
                    "li"
                )

                for price in product_prices:
                    type_price = price.find(
                        class_="fake mr-2 link-color price5").text.strip()
                    cur_price = price.find(class_="gray").text
                    product_price_obj[type_price] = re.search(r"\d+(?:[.]\d+)?", cur_price).group(0)

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

            product_info = {
                "Код товара": product_code,
                "Название": product_name,
                "Бренд товара": product_brand,
                "Артикул товара": product_article,
                "Цены товара": product_price_obj,
                "Количество на складе": product_count,
            }

            # minIndex = None
            # if len(product_info["Цены товара"]) == {}:
            #     for index, res in enumerate(result_mas):
            #         if len(res["Цены товара"]) == 0:
            #             minIndex = index
            #             break
            #         if float(product_info["Цены товара"]["Розница"]) <= float(res["Цены товара"]["Розница"]):
            #             minIndex = index
            #             break
            # if minIndex != None: result_mas.insert(minIndex, product_info)
            # else: result_mas.append(product_info)
            result_mas.append(product_info)
        
        return result_mas
    
    def searchBenefit(self, excelInfo):
        autooptGoods = []

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(excelInfo["goods"], file, ensure_ascii=False)

        for goods in excelInfo["goods"]:
            print(goods["mainArtikul"])

            exel_count = goods["amount"]
            good_offers = self.get_product_info(goods["mainArtikul"])

            best_offer = {
                "Название": goods["name"],
                "Артикул": goods["mainArtikul"],
                "Цена": 0.00,
                "Количество": 0,
                "Источник": "АвтоАльянс",
                "Бренд": "",
            }
            current_price = 1000000000.00

            for offer in  good_offers:

                if type(offer['Цены товара']) == dict:

                    if type(offer['Количество на складе']) == int:
                        site_count = int(offer['Количество на складе'])
                    else:
                        site_count = 0

                    if int(exel_count) <= int(site_count):
                        
                        if float(offer['Цены товара']['Опт 3']) < float(current_price):
                            current_price = float(offer['Цены товара']['Опт 3'])

                            best_offer["Количество"] = offer['Количество на складе']
                            best_offer["Цена"] = current_price
                            best_offer["Артикул"] = offer["Артикул товара"]
                            best_offer["Бренд"] = offer["Бренд товара"]
                            best_offer["Название"] = offer["Название"]
                else:

                    for analog_offer in offer['Цены товара']:

                        if type(analog_offer['Количество']) == int:
                            site_count = int(analog_offer['Количество'])
                        else:
                            site_count = 0

                        if int(exel_count) <= int(site_count):
                            
                            if float(analog_offer['Цена']) < float(current_price):
                                current_price = float(analog_offer['Цена'])

                                best_offer["Количество"] = site_count
                                best_offer["Цена"] = current_price
                                best_offer["Артикул"] = offer["Артикул товара"]
                                best_offer["Бренд"] = offer["Бренд товара"]
                                best_offer["Название"] = offer["Название"]

                # print(type(offer['Цены товара']) == dict)

            autooptGoods.append(best_offer)

            with open("data1.json", "w", encoding="utf-8") as file:
                json.dump(autooptGoods, file, ensure_ascii=False)

            sleep_time = uniform(5, 7)
            sleep(sleep_time)
        


    

if __name__ == "__main__":
   app = EngineParser()
   app.run()
