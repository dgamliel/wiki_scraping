import os
import time
from bs4 import BeautifulSoup
import requests

def get_request():
    get = requests.get('https://wikipedia.org/wiki/H')

    return get.text

def main():

    html = get_request()

    html_soup = BeautifulSoup(html, "lxml")
    html_soup.prettify()


    for header in html_soup.find_all('h2'):
        print(header)

#    print (html)

if __name__ == '__main__': main()
