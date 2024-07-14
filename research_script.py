from bs4 import BeautifulSoup
import requests
from _google_search import search

# this project will conduct automated research on a keyword inputted by the user.
# the results will be stored in an excel spreadsheet(until i find a real db) and 
# presented in some sort of manner
# but baby steps: first I need to search the web for the top five results on a search

# sounds pretty simple, all I need to do is use googlesearch to get the top five results,
# and search their headers for a description of the page. that'll be enough for the first
# version. Goodluck future me!

# start time: 10:15 PM 12/11/23
# emd time: 10:25 PM 12/11/23


query = input("enter research query: ")

print("results: ")

# uses googlesearch to get the first urls that come up
for i in search(query, num_results=1 ):
    print(i)
    page = requests.get(i)
    soup = BeautifulSoup(page.content, "html.parser")
# send head metadata to table