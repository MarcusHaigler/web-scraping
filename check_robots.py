# testing check_robots fuction

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

def check_robots(url_list): # check robots.txt for permission
  os.system("cls||clear")
# loop thru list 
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

print(check_robots(sample_urls))