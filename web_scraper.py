from urllib.request import urlopen
from googlesearch import search
import urllib.robotparser as urobot
import urllib.request
from bs4 import BeautifulSoup
import os

def google_search(query):
   for u in search(str(query), num_results=5):
      os.system('cls||clear')
      print(u)
      urls.append(u)
      print(f"progress: {len(urls)} / 5")
      if len(urls) == 5:
         print("all urls fetched")

def check_robots(url): # check robots.txt
   global url_robot
   global l
   for i in url: # read trhu url and find the end of the domain
      if url.index(i, i+3) != ".com":
         pass
      else:
         l = url.index(0,i+3)
         url_robot = url.index(0,i+3) # save as variable
         print(f"robots.txt found at {url_robot}")
   # read txt file and find look for the value    
      
urls = []
search_query = "cats" # make this an input for final version

google_search(search_query)
print(urls) # for testing

for url in urls:
   check_robots(url)
