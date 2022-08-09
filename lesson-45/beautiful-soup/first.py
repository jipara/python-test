from bs4 import BeautifulSoup


with open(file="website.html") as data:
    contents = data.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
print(soup.prettify())

print(soup.p)

all_anchore_tags = soup.find_all(name="a")
print(all_anchore_tags)

for tag in all_anchore_tags:
    print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)


heading_class = soup.find(name="h3", class_="heading")
print(heading_class.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

print(soup.select(selector=".heading"))
