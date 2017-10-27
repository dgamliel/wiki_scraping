#!/usr/bin/python3

import os
import time
from bs4 import BeautifulSoup
import requests

'''
This prompts the user to input what they want to search
and creates the search link (not case sensitive) to pass to the python requests 
function

Ex: in: Poison dart frogs --> Poison_Dart_Frogs
'''

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


'''
Takes in the wiki string and
sends a get request to the wiki server with the specific link

Ex: Get --> https://wikipedia.org/wiki/Poison_Dart_Frogs

This returns the HTML content of the wiki page
'''

def get_request(in_str):
    link_addr = "https://wikipedia.org/wiki/" + in_str
    get = requests.get(link_addr)
    
    return get.content

'''
This pulls the resources from the HTML data
Strings is the 
'''
def OL_string_parser(OL):
    for li in OL:
        for string in li.strings:
            #if len(string) > 2 or string != '^' or string != '.':
            print (string)

def main():
    in_string = input('What would you like to """cite"""? ')
    search_link = link_searcher(in_string)
    html = get_request(search_link)

    html_soup = BeautifulSoup(html, "lxml")
    html_soup.prettify()
    
    refrences_OL = html_soup.find_all('ol', {'class':'references'})

    OL_string_parser(refrences_OL)

if __name__ == '__main__': main()
