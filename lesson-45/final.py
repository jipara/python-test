from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
move_page = response.text

soup = BeautifulSoup(move_page, "html.parser")
list = soup.find_all(name="h3", class_="title")
fist = soup.find(name="h3", class_="title")
print(fist.getText())
#print(fist.getText().split(")"))
lists_of_movies = []


for one in list:
    movie_list = one.getText()
    lists_of_movies.append(movie_list)
lists_of_movies.reverse()
#print(lists_of_movies)

#new_list = []
#article_upvotes = [int(score.getText().split()[0] )for score in soup.find_all(name="span", class_="score")]

with open("movies.txt", "w") as f:
    last_list = []
    for element in lists_of_movies:
        new_last_list = f.writelines(element + "\n")



###or

movie_titles = [movie.getText() for movie in lists_of_movies]

### reverst back list
#start stop step
movie_titles[::-1]

#####3

for n in range(len(movie_titles) - 1, -1, -1):
    movie_titles[n]

movies = movie_titles[::-1]
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
