import requests
from bs4 import BeautifulSoup
import pandas as pd
brandname=[]
branddetail=[]
brandprice1=[]
branddiscount1=[]
for r in range(1,11):
    url="https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=+str(r)"
    page=requests.get(url)
    scrap=BeautifulSoup(page.text,"lxml")

    a=scrap.find("div",class_="_1YokD2 _2GoDe3")
    brand=a.find_all("div",class_="_2WkVRV")
    for r in brand:
        x=r.text
        brandname.append(x)

    branddetai=a.find_all("a",class_="IRpwTa")
    for r in branddetai:
        x=r.text
        branddetail.append(x)

    brandprice=a.find_all("div",class_="_30jeq3")
    for r in brandprice:
        x=r.text
        brandprice1.append(x)

    branddiscount=a.find_all("div",class_="_3Ay6Sb")
    for r in branddiscount:
        x=r.text
        branddiscount1.append(x)

s=pd.DataFrame({"brand_name":brandname,"brand_detail":branddetail,"brand_price":brandprice1,"brand_discount":branddiscount1})
s.to_csv("flipkart_shoes.csv")