Filmweb.pl Web Scraper

This Python script automates the process of scraping movie data from Filmweb.pl. It uses Selenium with a headless Chrome driver to retrieve specific details about each film including the name, year, duration, ranking, and genre.
Dependencies

    Selenium (pip install selenium)
    Pandas (pip install pandas)

Note: The script requires a ChromeDriver to be installed and added to PATH. Download it from the official site.
Structure of the Script

The script is divided into several functions to streamline the scraping process:

    get_driver(): Initializes a headless Chrome webdriver with an implicit wait of 10 seconds.

    scrape_links(driver, limit_pages=True): Scrapes the links of individual movie pages from the movie ranking on Filmweb.pl. It defaults to the first five pages but can be adjusted to scrape up to 500 pages.

    scrape_details(driver, links): Takes the list of links from scrape_links() and visits each link to scrape details about the film such as the name, year, duration, ranking, and genre.

Finally, the script compiles these film details into a pandas DataFrame and prints it to the console.
Usage

Navigate to the directory containing the script and run the following command:

bash

python3 main.py

The output is a pandas DataFrame printed to the console, representing the scraped data. Each row corresponds to a film, and the columns represent the film's details.
Further Development

This script is currently designed for scraping publicly available data from Filmweb.pl. Further improvements could include the addition of command-line arguments for user input, an option to save the DataFrame to a CSV file, or extending the script to handle more complex scraping tasks.
