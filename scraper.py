#!/usr/bin/env python3

from imgurpython import ImgurClient
from pprint import pprint
from helpers import get_input, get_config 
import requests, argparse, json
from selenium import webdriver


# Set up command-line arguments
parser = argparse.ArgumentParser('scraper.py')
parser.add_argument('query', help='Search query')
parser.add_argument('destination', help='Download destination')
args = parser.parse_args()

# Authenticate function
def authenticate():
    config = get_config()
    config.read('auth.ini')
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)

    return client

def search(query):
   galleries = []
   browser = webdriver.Firefox()
   browser.get(query)
   for gallery in browser.find_elements_by_class_name('image-list-link'):
       link = gallery.get_attribute('href')
       galleries.append(link)
   browser.quit()
   return galleries

def scrape_album(gallery, destination):
    # TODO - download images in the gallery to the destination folder
    print(gallery)


if __name__ == '__main__':
 #   client = authenticate()

    galleries = search(args.query)

    for gallery in galleries:
        scrape_album(gallery, args.destination)
