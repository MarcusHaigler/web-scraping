from urllib.request import urlopen
from google import search

def page_html(url):
   # read and decode page into html
   page = urlopen(url)
   html_bytes = page.read()
   html = html_bytes.decode("utf-8")
   
   return html

def google_search_results(query, pages):
   pages = []
   for url in search(query):
      pages.append(url)

   print(pages)
   return pages
   
def scrape_page(page):
   # scrapes page html for metadata
   pass

urls = []
search_query = input("enter search query: ")

google_search_results(search_query, urls)# gather top results
page_html(urls)# read html
scrape_page()