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

def check_robots(url): # check robots.txt
   os.system("cls||clear")
   print('checking robots for {ur}')
   end = '/'
   robot_url = ""
   can_fetch_status = False
   for i in url: # read thru url and find the end of the domain
      if url.index(i) != end:
         pass
      else:
         robot_url = url.index(0,i) + 'robots.txt'
         print(f"robot.txt: {robot_url}")
# read txt file for general rules   
   urlbot.RobotFileParser()
   urlbot.set_url(robot_url)
   urlbot.read()
   if urlbot.can_fetch("*", url):
      can_fetch_status =  True
   else:
      can_fetch_status =  False
   
   return can_fetch_status

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
