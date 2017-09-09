import os
import time
from bs4 import BeautifulSoup
import requests

def get_request():
    get = requests.get('https://wikipedia.org/wiki/H')

    return get.content

def main():

    html = get_request()

    html_soup = BeautifulSoup(html, "lxml")
    html_soup.prettify()
    
    refrences_OL = html_soup.find_all('ol', {'class':'references'})

    for list_item in refrences_OL:
        for li in list_item.find_all('li'):
            for ref-text in li.find_all('span', {'class','reference-text'}):
                print(ref-text)

if __name__ == '__main__': main()
