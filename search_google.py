# testing google_search function

from googlesearch import search
import os

def google_search(query):
   for u in search(str(query), num_results=5):
      os.system('cls||clear')
      print(u)
      urls.append(u)
      print(f"progress: {len(urls)} / 5")
      if len(urls) == 5:
         print("all urls fetched")

urls = []
search_query = "cats" # make this an input for final version

google_search(search_query)
print(urls) # for testing