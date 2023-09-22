from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
h3_tags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
h3_tags = h3_tags[::-1]
for movie in h3_tags:
    with open('movies.txt', 'a') as file:
        file.write(movie.getText())
        file.write("\n")
