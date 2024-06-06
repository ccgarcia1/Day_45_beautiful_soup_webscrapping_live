from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/").text

#print(response)

soup = BeautifulSoup(response, "html.parser")

#print(soup.title)
#getting the first tag text link and upvote
article_text = soup.find(name="span", class_="titleline").getText()
article_link = soup.find(name="span", class_="titleline").find("a").get("href")
article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)

# getting all the articled os the page
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.find("a").get("href"))

#print(f"texts: {len(article_texts)}")

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#print(article_upvotes)
#print(article_texts[0])
big_score_idx = article_upvotes.index(min(article_upvotes))

print(big_score_idx)

print(article_texts[big_score_idx])
print(article_links[big_score_idx])
print(article_upvotes[big_score_idx])

