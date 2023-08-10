from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

def get_driver(limit_pages=True):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    return driver

def scrape_links(driver, limit_pages=True):
    links = []

    for page in range(1, 6 if limit_pages else 501):  # 500 is the maximum number of pages
        driver.get(
            f"https://www.filmweb.pl/ranking/film?fbclid=IwAR0qC8KuR4Z159TFqObUBnv3jETlH6yKX7tgtovXJqxrMRs3bG0veCpA4wQ&page={page}")

        elements = driver.find_elements(By.CSS_SELECTOR, '.efficientPoster.rankingType__poster.EfficientPoster a')

        for el in elements:
            link = el.get_attribute('href')
            links.append(link)

    return links

def scrape_details(driver, links):
    films = []

    for link in links:
        driver.get(link)

        name = driver.find_element(By.CSS_SELECTOR, '.filmCoverSection__title').text
        year = driver.find_element(By.CSS_SELECTOR, '.filmCoverSection__year').text
        duration = driver.find_element(By.CSS_SELECTOR, '.filmCoverSection__duration').text
        ranking = driver.find_element(By.CSS_SELECTOR, '.filmRating__rateValue').text
        genre = driver.find_element(By.CSS_SELECTOR, 'div[itemprop="genre"] a').text

        films.append({
            'name': name,
            'year': year,
            'duration': duration,
            'ranking': ranking,
            'genre': genre,
        })

    return films


driver = get_driver()
links = scrape_links(driver)
films = scrape_details(driver, links)

df = pd.DataFrame(films)
print(df)

