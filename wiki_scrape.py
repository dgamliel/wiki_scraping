import os
import time
from bs4 import BeautifulSoup
import requests

def get_request():
    get = requests.get('https://wikipedia.org/wiki/Poison_Dart_Frogs')

    return get.content

def main():

    html = get_request()

    html_soup = BeautifulSoup(html, "lxml")
    html_soup.prettify()
    
    refrences_OL = html_soup.find_all('ol', {'class':'references'})
    for list_item in refrences_OL:
        for li in list_item.find_all('li'):
            ref_text = li.find('span', {'class','reference-text'})
            print(ref_text)
            print('\n')

if __name__ == '__main__': main()
