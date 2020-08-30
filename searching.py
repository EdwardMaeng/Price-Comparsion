from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.execptions import TimeoutException

import re
import time


class Searching(object):
    
    def __init__(self, items):
        self.amazon_url = "https://www.amazon.ca/"
        self.ebay_url = 
        self.items = items

