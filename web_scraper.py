from urllib.request import urlopen
from googlesearch import search

def parse_html(url):
   # read and decode page into html
   page = urlopen(url)
   html_bytes = page.read()
   html = html_bytes.decode("utf-8")
   
   print("html parsed...")
   return html

def google_search_results(query, pages):
   pages = []
   for url in search(query, stop=3):
      pages.append(url)

   print("pages loaded...")
   return pages
   
def read_robots(url): # check robot.txt
   pass
   
   
def scrape_page(page):
   # scrapes page html for metadata
   pass

urls = []
search_query = input("enter search query: ")

google_search_results(search_query, urls)# gather top results
### for website in urls:
parse_html(urls)# read html
   
# scrape_page()