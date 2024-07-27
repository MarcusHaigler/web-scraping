# testing check_robots fuction

from urllib.request import urlopen
from googlesearch import search
import urllib.robotparser
import os

sample_urls = ['https://www.imdb.com/title/tt5697572/', 'https://www.reddit.com/r/cats/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/']

def check_robots(url): # check robots.txt
   os.system("cls||clear")
   print(f'checking robots for {url}')
   end = '/'
   robot_url = ""
   can_fetch_status = False

# read thru url and find the end of the domain
    
      

# read txt file for general rules   
   urlbot = urllib.robotparser.RobotFileParser()
   urlbot.set_url(robot_url)
   urlbot.read()
   if urlbot.can_fetch("*", url):
      can_fetch_status =  True
   else:
      can_fetch_status =  False
   
   return can_fetch_status

for url in sample_urls:
   if check_robots(url) is True:
      pass
   else:
      # remove url from list
      sample_urls.remove(url)

# test point
print(f"usable urls:")
print(sample_urls)