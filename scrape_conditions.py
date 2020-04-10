import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def get_HTML(url):

    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    return soup

# Scraping Swell Data
def scrape_swell(soup):

    swell = soup.find_all('h4', 'nomargin font-sans-serif heavy')
    swell_list = []

    for i in range(len(swell)):
        swell_list.append(swell[i].text)

    return swell_list

# Separating Swell Size from swell list
def separate_swell_size(swell_list, unit_ft = 'ft'):

    swell_size = []

    for item in swell_list:
        if unit_ft in item:
            swell_size.append(item)

    swell_size = [item.replace(' ','') for item in swell_size]
    swell_size = [float(item.replace('ft','')) for item in swell_size]

    return swell_size

# Separating Swell Period from swell list
def separate_swell_period(swell_list, unit_s = 's'):

    swell_period = []

    for item in swell_list:
        if unit_s in item:
            swell_period.append(item)

    swell_period = [item.replace(' ','') for item in swell_period]
    swell_period = [int(item.replace('s','')) for item in swell_period]

    return swell_period

# Scraping Swell direction
def scrape_swell_direction_initial(soup, swell_dir_list1):

    swell_direction = soup.find_all('td',
                                    attrs={"class":"text-center msw-js-tooltip background-gray-lighter"})
    swell_dir_list = [item['title'] for item in swell_direction]+swell_dir_list1

    return swell_dir_list

def scrape_swell_direction_end(soup):

    swell_direction1 = soup.find_all('td',
                                     attrs={"class":"text-center msw-js-tooltip background-gray-lightest"})
    swell_dir_list1 = [item['title'] for item in swell_direction1]

    return swell_dir_list1

def toList(input_list):

    swell_direction_string = ""

    for item in input_list:
        swell_direction_string += item

    return swell_direction_string

def clean_string(input_string):

    cleaned_string = ""

    for character in input_string:
        if character.isnumeric():
            cleaned_string += character
        elif character == ',':
            cleaned_string += character

    return cleaned_string

def string_to_list(input_string):

    swell_direction_list = []
    i = 0

    while i <= len(input_string) - 1:
        swell_direction_list.append(int(input_string[i:i+3]))
        i += 3

    return swell_direction_list
