from scraping_ebay import Scraping_eBay
from scraping_walmart import Scraping_walmart
from scraping_bestbuy import Scraping_BestBuy

class scraping():

    def __init__(self, item):
        self._item_list = []
        ebay = Scraping_eBay(item)
        walmart = Scraping_walmart(item)
        bestbuy = Scraping_BestBuy(item)
        ebay.scrap()
        walmart.scrap()
        bestbuy.scrap()
        # Ebay
        ebay_dict = []
        name, price, image, item = ebay.find_low_price_index()
        print("Ebay name: ", name)
        print("Ebay price: ", price)
        print("Ebay image: ", image)
        print("Ebay item: ", item)
        ebay_dict.append(name)
        ebay_dict.append(price)
        ebay_dict.append(image)
        ebay_dict.append(item)
        ebay_dict.append("Ebay")
        # Walmart
        walmart_dict = []
        name, price, image, item = walmart.find_low_price_index()
        print("Walmart name: ", name)
        print("Walmart price: ", price)
        print("Walmart image: ", image)
        print("Walmart item: ", item)
        walmart_dict.append(name)
        walmart_dict.append(price)
        walmart_dict.append(image)
        walmart_dict.append(item)
        walmart_dict.append("Walmart")
        # Bestbuy
        bestBuy_dict = []
        name, price, image, item = bestbuy.find_low_price_index()
        print("Bestbuy name: ", name)
        print("Bestbuy price: ", price)
        print("Bestbuy image: ", image)
        print("Bestbuy item: ", item)
        bestBuy_dict.append(name)
        bestBuy_dict.append(price)
        bestBuy_dict.append(image)
        bestBuy_dict.append(item)
        bestBuy_dict.append("BestBuy")
        # Store items into list
        self._item_list.append(ebay_dict)
        self._item_list.append(walmart_dict)
        self._item_list.append(bestBuy_dict)
    
    def get_item_list(self):
        return self._item_list

myScrap = scraping("tv")