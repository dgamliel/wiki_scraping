import os
import time
from bs4 import BeautifulSoup
import requests

def link_searcher():
    in_string = input('What would you like to """cite"""?')
    in_string_list = in_string.split()
    for word in in_string_list:
        if len(word) > 1:
            word[0].capitalize()
            word[1:].lower()
        else:
            word.capitalize()

    return_string = '/'.join(in_string_list)

    return return_string

search_link = link_searcher()

def get_request():
    get = requests.get('https://wikipedia.org/wiki/Gay')

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
