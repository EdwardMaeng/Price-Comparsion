import requests, time
from searching import giveURL
from bs4 import BeautifulSoup
from re import sub

headers = {
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
    }

URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=camera"
name_container = []
price_container = []
imagelink_container = []
headers = headers
print("Downloading %s"% URL)
page = requests.get(URL, headers=headers)
if page.status_code > 500:
    if "To discuss automated access to eBay data please contact" in page.text:
        print("Page %s was blocked by eBay. Please try using better proxies\n"% URL)
    else:
        print("Page %s must have been blocked by eBay as the status code was %d"%(URL, page.status_code))
soup = BeautifulSoup(page.content, 'html.parser')

name_container += soup.findAll("span", {"class":"s-item__title"})
price_container += soup.findAll("span", {"class":"s-item__price"})

for i in range(len(name_container)):
    print("Name: ", name_container[i].get_text())
for i in range(len(price_container)):
    print("Price: $", price_container[i].get_text())
