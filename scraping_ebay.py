import requests, time
from searching import giveURL
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal

headers = {
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
    }

class Scraping_eBay():

    def __init__(self, item):
        self.URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=" + item
        self.name_container = []
        self.price_container = []
        self.imagelink_container = []
        self.headers = headers
        # make sure the request gets sent properly
        print("Downloading %s"%self.URL)
        self.page = requests.get(self.URL, headers=headers)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def scrap(self):
        self.name_container += self.soup.findAll("h3", {"class":"s-item__title"})
        self.price_container += self.soup.findAll("span", {"class":"s-item__price"})     

    def find_low_price_index(self):
        temp_p, temp_n = self.convert_price()
        price = min(temp_p)
        minpos = temp_p.index(price)
        return self.name_container[minpos].get_text(), price
            
    def convert_price(self):
        print("Initiating convert_price()")
        new_p, d_name, i = [], [], 0
        for p in self.price_container:
            temp = p.get_text()
            if not ('to' in temp or 'Tap' in temp):
                new_p += [Decimal(sub(r'[^\d.]', '', temp))]
        return new_p, d_name
    
    def print(self):
        print("Initiating print()")
        for i in range(len(self.name_container)):
            print("Name: ", self.name_container[i].get_text())
            print("Price: $", self.price_container[i].get_text())


s = Scraping_eBay("camera")
s.scrap()
name, price = s.find_low_price_index()
print("Name:", name, "--> $", price)