import requests, time
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal

headers = {
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
    }

class Scraping_walmart():

    def __init__(self, item):
        self.URL = "https://www.walmart.com/search/?query=" + item
        self.item = item
        self.name_container = []
        self.price_container = []
        self.imagelink_container = []
        self.itemlink_container = []
        self.headers = headers
        # make sure the request gets sent properly
        print("Downloading %s"%self.URL)
        self.page = requests.get(self.URL, headers=headers)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def scrap(self):
        temp = self.soup.findAll("a", {"class":"product-title-link line-clamp line-clamp-2 truncate-title"})
        temp_list = []
        for h4 in temp:
            temp_list += h4.find('span')
        for nc in temp_list:
            if not self.item in nc:
                self.name_container.append(nc)
        self.price_container += self.soup.findAll("span", {"class":"price-characteristic"})
        for link in self.soup.findAll("img", {"data-pnodetype":"item-pimg"}):
            self.imagelink_container.append(link.get('data-image-src'))
        for link in self.soup.findAll("a", {"lang": "en"}):
            self.itemlink_container.append(link.get('href'))     

    def find_low_price_index(self):
        temp_p, temp_n = self.convert_price()
        price = min(temp_p)
        minpos = temp_p.index(price)
        return self.name_container[minpos], price, self.imagelink_container[minpos], self.itemlink_container[minpos]
            
    def convert_price(self):
        print("Initiating convert_price()")
        new_p, d_name, i = [], [], 0
        if len(self.price_container) <= len(self.name_container): l = len(self.price_container)
        else: l = len(self.name_container)
        for i in range(l):
            temp = self.price_container[i].get_text()
            if not ('to' in temp or 'Tap' in temp):
                new_p += [Decimal(sub(r'[^\d.]', '', temp))]
        return new_p, d_name
    
    def print(self):
        print("Initiating print()")
        for i in range(len(self.price_container)):
            print("Name: ", self.name_container[i])
            print("Price: $", self.price_container[i].get_text())
            print("Image Link:", self.imagelink_container[i])
            print("Item Link:", self.itemlink_container[i])


# s = Scraping_walmart("camera")
# s.scrap()
# name, price, image, item = s.find_low_price_index()
# print("Name:", name, "--> $", price)