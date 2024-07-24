from urllib.request import urlopen
from googlesearch import search
import urllib.robotparser as urlbot
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
   end = '/'
   robot_url = ""
   for i in url: # read thru url and find the end of the domain
      if url.index(i) != end:
         pass
      else:
         robot_url = url.index(0,i) + '/robots.txt'
         print(f"robot.txt: {robot.url}")
# read txt file and find look for the value    
   urlbot.RobotFileParser()
   urlbot.set_url(robot_url)
   urlbot.read()
   if urlbot.can_fetch("*", url):
      return True
   else:
      return False
urls = []
search_query = "cats" # make this an input for final version

google_search(search_query)
print(urls) # for testing

for url in urls:
   if check_robots(url) is 
   
   
