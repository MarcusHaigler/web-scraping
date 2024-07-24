from urllib.request import urlopen
from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
import os

import urllib.robotparser as urobot
import urllib.request

import requests

def status_code(url):
    r = requests.get(url)
    return r.status_code

def google_search(query):
   for u in search(str(query), num_results=5):
      os.system('cls||clear')
      print(u)
      urls.append(u)
      print(f"progress: {len(urls)} / 5")
      if len(urls) == 5:
         print("all urls fetched")

def check_robots(url): # check robots.txt
### find the robots.txt file and check for disallows
# if 
   for i in url: # read thruu url and find the end of the domain
      if url.index(i, i+3) != ".com":
         pass
      else:
         robot_txt = url.index(0,i+3) # save as variable
   # read txt file and find look for the value
   rp = urobot.RobotFileParser()
   rp.set_url(robot_txt + '/robots.txt')
   rp.read()

   if rp.can_fetch('*', url):
      site = urllib.request.urlopen(url)
      sauce = site.read()
      soup = BeautifulSoup(sauce, '')

urls = []
search_query = "cats" # make this an input for final version

google_search(search_query)
print(urls) # for testing

# for url in urls:
#   check_robots(url)
