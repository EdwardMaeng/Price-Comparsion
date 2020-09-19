import requests, time
from searching import giveURL
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
        self.headers = headers
        # make sure the request gets sent properly
        print("Downloading %s"%self.URL)
        self.page = requests.get(self.URL, headers=headers)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def scrap(self):
        #<a lang="en" class="product-title-link line-clamp line-clamp-2 truncate-title" href="/ip/Google-Nest-Cam-Indoor-Security-Camera/45806610?wpa_bd=&amp;wpa_pg_seller_id=F55CDC31AB754BB68FE0B39041159D63&amp;wpa_ref_id=wpaqs:Pp4qgNm1k6VYKphGITh56S5j7e2ViRC6_a_TfT3h2J1IYPgQAsp6jmUmkwzZFwGZ9YYJoTUwhNTE3zkULQJUAzpPlxTnDpEyocuGj-Jwrk5zaQJ3QukQQmHt1JtrtfDAqupKPlht7AoCKZJRSSjHP1TO1FH-6g1FwzlyFWqRe6mDzHMqqhtpph_n-Gbvy_bQgzKxX13XFAzlUPETBi4QwednQZid4Z2LTO0Snc3OcZiVLVVEMhSWWTg38lLN_op8&amp;wpa_tag=&amp;wpa_aux_info=&amp;wpa_pos=1&amp;wpa_plmt=1145x1145_T-C-IG_TI_1-2_HL-INGRID-GRID-NY&amp;wpa_aduid=94ff67e6-3d2d-47d7-a3b4-d3a3fbffcd0e&amp;wpa_pg=search&amp;wpa_pg_id=camera&amp;wpa_st=camera&amp;wpa_tax=3944_133277&amp;wpa_bucket=__bkt__" tabindex="-1" data-type="itemTitles"><span>Google Nest Cam Indoor Security <mark>Camera</mark></span></a>
        temp = self.soup.findAll("a", {"class":"product-title-link line-clamp line-clamp-2 truncate-title"})
        temp_list = []
        for h4 in temp:
            temp_list += h4.find('span')
        for nc in temp_list:
            if not self.item in nc:
                self.name_container.append(nc)
        #<span class="price-characteristic">129</span>
        self.price_container += self.soup.findAll("span", {"class":"price-characteristic"})     

    def find_low_price_index(self):
        temp_p, temp_n = self.convert_price()
        price = min(temp_p)
        minpos = temp_p.index(price)
        return self.name_container[minpos], price
            
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
        print(len(self.name_container), len(self.price_container))
        for i in range(len(self.price_container)):
            print("Name: ", self.name_container[i])
            print("Price: $", self.price_container[i].get_text())


# s = Scraping_walmart("camera")
# s.scrap()
# name, price = s.find_low_price_index()
# print("Name:", name, "--> $", price)