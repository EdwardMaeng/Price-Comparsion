from searching import giveURL
import requests, time
from bs4 import BeautifulSoup

URL = giveURL()

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("span", {"class":"a-price-whole"})
time.sleep(3)
print(containers)


# for container in containers:
#     brand = containers.div.div.a.img["title"]
#     print("brand: " + brand)

#product_name = soup.find(id="productTitle").get_text()
#product_price = soup.find(id="priceblock_ourprice").get_text()
#product_imagelink = soup.find(id="imgTageWrapperID").get_text()

#converted_price = float(product_price[1:6])

#print(product_name.strip())
#print(converted_price)