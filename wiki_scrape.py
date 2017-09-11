#!/usr/bin/python3

import os
import time
from bs4 import BeautifulSoup
import requests

def link_searcher(in_string):
    # in_string = input('What would you like to """cite"""?')
    in_string_list = in_string.split()
    ret_list = []
    for word in in_string_list:
        if len(word) > 1:
            word = word[0].capitalize() + word[1:].lower()
        else:
            word = word.capitalize()
        ret_list.append(word)

    return_string = '_'.join(ret_list)

    return return_string

# search_link = link_searcher()

def get_request(in_str):
    link_addr = "https://wikipedia.org/wiki/" + in_str
    get = requests.get(link_addr)

    return get.content

def main():
    in_string = input('What would you like to """cite"""? ')
    search_link = link_searcher(in_string)
    html = get_request(search_link)

    html_soup = BeautifulSoup(html, "lxml")
    html_soup.prettify()
    
    refrences_OL = html_soup.find_all('ol', {'class':'references'})

    if len(refrences_OL) == 0:
        print("No references found")
        return

    for list_item in refrences_OL:
        for li in list_item.find_all('li'):
            ref_text = li.find('span', {'class','reference-text'})
            print(ref_text)
            print('\n')

if __name__ == '__main__': main()
