from scraping_ebay import Scraping_eBay
from scraping_walmart import Scraping_walmart
#from scraping_bestbuy import Scraping_BestBuy
import searching

def Scraping():
    item = searching.giveURL()
    ebay = Scraping_eBay(item)
    walmart = Scraping_walmart(item)
    #bestbuy = Scraping_bestbuy(item)

    ebay.scrap()
    walmart.scrap()
    #bestbuy.scrap()

    name1, price1 = ebay.find_low_price_index()
    name2, price2 = walmart.find_low_price_index()
    #name3, price3 += bestbuy.find_low_price_index()

    min_price = min(price1, price2)

    if min_price == price1:
        print("From eBay --> Name:", name1, "    $", price1)
        return 'eBay', name1, price1
    elif min_price == price2:
        print("From Walmart --> Name:", name2, "    $", price2)
        return 'Walmart', name2, price2
    # elif min_price == price3:
    #     print("From BestBuy --> Name:", name3, "    $", price3)
    #     return 'BestBuy', name3, price3
    else:
        print("No Product Found")
        return