# testing check_robots fuction

from urllib.request import urlopen
from googlesearch import search
import urllib.robotparser
import os

sample_urls = ['https://www.imdb.com/title/tt5697572/', 'https://www.reddit.com/r/cats/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/', 'https://www.imdb.com/title/tt5697572/']

def get_home_page(word):
  hp = word[12:] # cut off the 'https://www.'
  end_value = '/' # the end of the url name
  captured_url = ""
# loop thru the rest of the url and find the end value
  for i in hp:
    print(i)
    if i != end_value:
      pass
    else:
      captured_url = hp[:i]

      return captured_url
    
    return False
    
def check_robots(url_list): # check robots.txt for permission
   os.system("cls||clear")
   
   print(f'checking robots for {url}')
   robot_url = ""
   can_fetch_status = False
  
# integrate get_home_page here to find the end of the url homepage
   if get_home_page(url) is False:
    print("url capture failed")
    
   else:
    print("url capture successful")
    robot_url = get_home_page(url)
    
    # read txt file for general rules   
    urlbot = urllib.robotparser.RobotFileParser()
    urlbot.set_url(robot_url)
    urlbot.read()
    if urlbot.can_fetch("*", url):
        can_fetch_status =  True
    else:
        can_fetch_status =  False
    
    return can_fetch_status

for url in sample_urls: # remove all websites that dont allow web scraping
   if check_robots(url) is True:
      pass
   else:
      # remove url from list
      sample_urls.remove(url)

# test point
print(f"usable urls:")
print(sample_urls)