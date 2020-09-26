from scraping_ebay import Scraping_eBay
from scraping_walmart import Scraping_walmart
from scraping_bestbuy import Scraping_BestBuy
import searching

item = searching.giveURL()
ebay = Scraping_eBay(item)
walmart = Scraping_walmart(item)
bestbuy = Scraping_BestBuy(item)
ebay.scrap()
walmart.scrap()
bestbuy.scrap()

def scrap_ebay():
    name, price, image, item = ebay.find_low_price_index()
    print("From eBay --> Name:", name)
    print("$", price)
    print("Image:", image)
    print("Item:", item)
    return name, price, image, item

def scrap_walmart():
    name, price, image, item = walmart.find_low_price_index()
    print("From Walmart --> Name:", name)
    print("$", price)
    print("Image:", image)
    print("Item:", item)
    return name, price, image, item

def scarp_bestbuy():
    name, price, image, item = bestbuy.find_low_price_index()
    print("From BestBuy --> Name:", name)
    print("$", price)
    print("Image:", image)
    print("Item:", item)
    return name, price, image, item

scrap_ebay()
scrap_walmart()
scarp_bestbuy()