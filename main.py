from bs4 import BeautifulSoup
import requests
search = input(" Enter your search term ")
param = {"q": search}
r = requests.get("https://www.bing.com/search", params=param)
soup = BeautifulSoup(r.text)
print(soup.prettify())