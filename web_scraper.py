from urllib.request import urlopen
from googlesearch import search
import urllib.robotparser as urlbot
import urllib.request
from bs4 import BeautifulSoup
import os

import requests

def status_code(url):
    r = requests.get(url)
    return r.status_code

def google_search(query):
   for u in search(str(query), num_results=1):
      os.system('cls||clear')
      print(u)
      urls.append(u)
      print(f"progress: {len(urls)} / 5")
      if len(urls) == 5:
         print("all urls fetched")

from urllib.request import urlopen
from googlesearch import search
import urllib.robotparser
import os

sample_urls = ['https://www.imdb.com/title/tt5697572/', 'https://www.reddit.com/r/cats/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/']

sample = 'https://www.imdb.com/title/tt5697572/'

def get_robots(link):
  url = link[12:]
  end_value = '/'
  robots_link = ""

  for l in url:
    if l is end_value:
      end = url.index(l)
      robots_link = "https://" + url[:end] + "/robots.txt"
      return robots_link

def check_robots(url_list): # check robots.txt for permissions
  for url in url_list:
    print(f'checking robots for {url}')
    robot_url = ""
# pull homepage url  
    if get_robots(url) is False:
      print("url capture failed")
      break
    else:
      print("url capture successful")
      robot_url = get_robots(url)
# read robots.txt file for general rules   
      urlbot = urllib.robotparser.RobotFileParser()
      urlbot.set_url(robot_url)
      urlbot.read()
# if it allows bots, keep in list, if not, remove it
      if urlbot.can_fetch("*", url):
        pass
      else:
        url_list.remove(url)
# return modified list
  return url_list

def scrape_page(url):
   pass

urls = []
search_query = "cats" # make this an input for final version

# # # START OF PROGRAM # # #
google_search(search_query)
print(urls) # for testing

for url in urls:
   if check_robots(url) is True:
      pass
   else:
      # remove url from list
      urls.remove(url)

# test point
print(f"usable urls:")
print(urls)
# scrape html from each page and save in txt files
