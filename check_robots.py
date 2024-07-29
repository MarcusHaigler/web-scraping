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
# loop thru list 
  for url in url_list:
    print(f'checking robots for {url}')
    robot_url = ""
    can_fetch_status = False
# pull homepage url  
    if get_home_page(url) is False:
      print("url capture failed")
      break
    else:
      print("url capture successful")
      robot_url = get_home_page(url)
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

check_robots(sample_urls)