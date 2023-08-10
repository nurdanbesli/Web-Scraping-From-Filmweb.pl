To run the code, follow these steps:
 - Open a terminal or command prompt.
 - Make sure you have Scrapy installed. If not, install it using the command: pip install scrapy
 - Create a new Scrapy project using the command: scrapy startproject myproject
 - Place the spiders provided in the appropriate "spiders" folder within your Scrapy project directory.
 - Navigate to your Scrapy project directory.
 - Execute the command: scrapy crawl link_lists -o links.csv to run the "link_lists" spider and save the extracted links to a CSV file named "links.csv".
 - After the above step, execute the command: scrapy crawl films -o films.csv to run the "films" spider and save the scraped movie data to a CSV file named "films.csv".
 - Verify the generated CSV files ("link_list.csv" and "films.csv") to check if the data has been successfully scraped.
