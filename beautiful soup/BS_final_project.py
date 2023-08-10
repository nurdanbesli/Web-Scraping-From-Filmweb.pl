import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Function to scrape movie data from a given movie URL
def scrape_movie_data(movie_url):
    response = requests.get(movie_url)
    soup = bs(response.content, 'html.parser')

    title = soup.find('h1', class_='filmCoverSection__title', itemprop='name').text.strip()
    rating = soup.find('span', class_='filmRating__rateValue').text.strip()
    year = soup.find('div', class_='filmCoverSection__year').text.strip()
    genre = soup.find('div', class_='filmInfo__info', itemprop='genre').text.strip()
    duration = soup.find('div', class_='filmCoverSection__duration', itemprop='timeRequired').text.strip()

    film = {
        'title': title,
        'year': year,
        'duration': duration,
        'rating': rating,
        'genre': genre,
    }
    return film

# Send a GET request to the main ranking page
url = "https://www.filmweb.pl/ranking/film"

films = []

# Iterate over each page of the rankings
for page in range(1, 6):  # Change the range as per the number of pages you want to scrape
    page_url = f"{url}?page={page}"
    response = requests.get(page_url)
    soup = bs(response.content, 'html.parser')

    # Find the movie list on the page
    movie_list = soup.find_all('h2', class_='rankingType__title')

    # Iterate over each movie and extract the link
    for movie in movie_list:
        movie_link = movie.find_next('a')['href']
        movie_url = f"https://www.filmweb.pl{movie_link}"
        print("Scraping data from:", movie_url)
        film_data = scrape_movie_data(movie_url)
        films.append(film_data)
        print("Data scraped successfully!")

df = pd.DataFrame(films)
