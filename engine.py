import pandas as pd
import openpyxl as op
from openpyxl import load_workbook

#Делаем по видео openpyxl
# book = op.open("./konkurs_32413759336.xlsx")
# sheet = book.active

# print(sheet[10][10].value)

# Читаем с openpyxl
wb = load_workbook("./konkurs_32413759336.xlsx", data_only=True)
sheet = wb.active

df = pd.DataFrame(sheet.values)
# while df.loc[0, 1] == None:
#     df = df.drop([0])
# for row in df.iterrows()
# print(df None)

df.apply(lambda check: print(check.isna(), "\n", '----------------'), 1)



# if df.loc[0, 1] == None:# Еще читаем с openpyxl

# for cellObj in sheet["A1":"C2"]:
#     for cell in cellObj:
#         print(cell.coordinate, cell.value)
#     print("--END--")
    

# cwd = os.getcwd()

# os.chdir("e:/")

# print(cwd)

# file = "konkurs_32413759336.xlsx"
# xl = pd.ExcelFile(file)

# print(xl.parse(xl.sheet_names)["title"])

# Читаем на чистом Pandas
# read = pd.read_excel("konkurs_32413759336.xlsx")
# table = read.head()
# print(table)

