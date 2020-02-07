#!/usr/bin/env python3

from imgurpython import ImgurClient
from pprint import pprint
from helpers import get_input, get_config 
import requests, argparse, json

# Set up command-line arguments
parser = argparse.ArgumentParser('scraper.py')
parser.add_argument('query', help='Search query')
parser.add_argument('max_galleries', defualt='0', help='Maximum albums to scrape')
parser.add_argument('-v', '--verbose', default=False, help='Turn on verbose output')
args = parser.parse_args()

# Authenticate function
def authenticate():
    config = get_config()
    config.read('auth.ini')
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)

    return client

def search(query, max_galleries)
   #TODO: Search for a number of galleries that match the query
   #TODO: accumulate the galleries found into a list 'galleries'

   return galleries

def scrape_album(gallery):
    # TODO - download images in the gallery

if __name__ == '__main__':
    client = authenticate()

    galleries = search(args.query, args.max_galleries)

    for gallery in galleries:
        scrape_album(gallery)
