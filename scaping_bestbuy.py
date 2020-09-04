import requests, time
from searching import giveURL
from bs4 import BeautifulSoup
from re import sub

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44',
        'authority': 'www.bestbuy.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
    }

class Scraping_BestBuy():

    def __init__(self, item):
        self.URL = "https://www.bestbuy.com/site/searchpage.jsp?st=" + item
        self.name_container = []
        self.price_container = []
        self.imagelink_container = []
        self.headers = headers
        # make sure the request gets sent properly
        print("Downloading %s"%self.URL)
        self.page = requests.get(self.URL, headers=headers)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def scrap(self):
        temp = self.soup.findAll("h4", {"class":"sku-header"})
        for h4 in temp:
            self.name_container += h4.find('a')

        temp = self.soup.findAll("div", {"class":"priceView-hero-price priceView-customer-price"})
        for div in temp:
            firstSpan = next(div.children, None)
            if firstSpan:
                self.price_container.append(firstSpan.get_text())
        #self.price_container += self.soup.findAll("span", {"class":"a-offscreen"})
        #self.imagelink_container += self.soup.findAll("div", {"class":"a-section aok-relative s-image-fixed-height"})
        for i in range(3):
            self.price_container.pop(0)
        
        for name in self.name_container:
            print("Item Name: ", name)
        for price in self.price_container:
            print("Item Price: ", price)

        print(len(self.name_container))
        print(len(self.price_container))       

    #def find_low_prices(self):
            
    def convert_price(self):
        print("Initiating convert_price()")
        for p in self.price_container[:len(self.name_container)]:
            converted_price = float(p.get_text())
            self.price_container.remove(p)
            self.price_container.append(converted_price)
    
    def print(self):
        print("Initiating print()")
        for i in range(len(self.name_container)):
            print("Name: ", self.name_container[i].get_text())
            print("Price: $", self.price_container[i].get_text())
    
    #def __repr__():
    #def __str__():

s = Scraping_BestBuy("camera")
s.scrap()
s.convert_price()
s.print()