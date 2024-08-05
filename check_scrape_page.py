from bs4 import BeautifulSoup
import requests

page = sample = 'https://www.imdb.com/title/tt5697572/'

result = requests.get(page)

print(result)
