import requests, time
from searching import giveURL
from bs4 import BeautifulSoup
from re import sub

# Find what they are using
# Then, Store those into dictionary / List
companyPreferences = {"amazon":"a-size-medium a-color-base a-text-normal", }

headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

class Scraping_Amazon():

    def __init__(self, item):
        self.URL = url() # change This
        self.name_container = []
        self.price_container = []
        self.imagelink_container = []
        self.headers = headers
        # make sure the request gets sent properly
        print("Downloading %s"%self.URL)
        self.page = requests.get(self.URL, headers=headers)
        if self.page.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in self.page.text:
                print("Page %s was blocked by Amazon. Please try using better proxies\n"% self.URL)
            else:
                print("Page %s must have been blocked by Amazon as the status code was %d"%(self.URL, self.page.status_code))
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def scrap(self):
        # temp = self.soup.findAll("div", {"data-index"})
        # anotherTemp = temp.findAll()
        self.name_container += self.soup.findAll("span", {"class":"a-size-medium a-color-base a-text-normal"})
        self.price_container += self.soup.findAll("span", {"class":"a-price-whole"})
        #self.price_container += self.soup.findAll("span", {"class":"a-offscreen"})
        #self.imagelink_container += self.soup.findAll("div", {"class":"a-section aok-relative s-image-fixed-height"})

    #def find_low_prices(self):   
            
    def convert_price(self):
        for p in self.price_container[:len(self.name_container)]:
            converted_price = float(p.get_text())
            self.price_container.remove(p)
            self.price_container.append(converted_price)
    
    def print(self):
        for i in range(len(self.name_container)):
            print("Name: ", self.name_container[i].get_text())
            print("Price: $", self.price_container[i].get_text())
    
    #def __repr__():
    #def __str__():

s = Scraping(giveURL)
s.scrap()
s.convert_price()
s.print()