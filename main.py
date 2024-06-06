from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/").text

print(response)

soup = BeautifulSoup(response, "html.parser")

print(soup.title)