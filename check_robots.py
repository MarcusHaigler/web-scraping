# testing check_robots fuction

from urllib.request import urlopen
from googlesearch import search
import urllib.robotparser
import os

sample_urls = ['https://www.imdb.com/title/tt5697572/', 'https://www.reddit.com/r/cats/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/']

def scan_url(word, end_value);
# take off the https part of the url here

# loop thru the rest of the url and find the end value
  for i in word:
    print(i)
    if i != end_value:
      print("False")
    else:
      print("True")
    
def check_robots(url): # check robots.txt
   os.system("cls||clear")
   print(f'checking robots for {url}')
   end = '/'
   robot_url = ""
   can_fetch_status = False
  
# integrate scan_url here to find the end of the url homepage
         
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