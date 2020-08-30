import time

def giveURL():
    print('Enter item:')
    item = input()
    URL = 'https://www.amazon.com/s?k=' + item
    return URL

