from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#title_link = soup.find_all(class_="titlelink")

# heading_class = soup.find_all(name="a", class_="titlelink")
# for text in heading_class:
#     print(text.getText())

# title_for_web_page = soup.find_all(name="a", class_="titlelink")
# print(title_for_web_page.getText())
#
articles = soup.find_all(name="a", class_="titlelink")
# print(title_for_web_page.getText())
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0] )for score in soup.find_all(name="span", class_="score")]
print(article_upvotes.index(max(article_upvotes)))
print(article_texts[0])
print(article_links[0])
# #article_upvote = soup.find(name="span", class_="score")
#
#
#
#
# ###or
# article_upvotes = soup.find_all(name="span", class_="score").getText()
# print(article_upvotes)


# article_test = article_upvotes[0].split(" ")
# point = int(article_test[0])
# print(type(point))

