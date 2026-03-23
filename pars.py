import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url="https://books.toscrape.com/"

response=requests.get(url)
html=response.text

soup=BeautifulSoup(html, "html.parser")

jpg=soup.find("p", class_="price_color")
all_price=soup.find_all("p", class_="price_color")

wb=Workbook()
ws=wb.active

ws['A1']='Название книги'
ws['B1']='Цена книги'

url1=f"https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
res=requests.get(url1)
html1=res.text

soup1=BeautifulSoup(html1, "html.parser")
all_name_books=soup1.find("div", class_="col-sm-6 product_main")

title=soup1.find("h1").text
price=soup1.find("p", class_="price_color").text

print(title, " : ", price)

ws['A2']=title
ws['B2']=price
wb.save("book_price.xlsx")