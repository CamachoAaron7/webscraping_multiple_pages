### SCRIPT FOR MULTIPLE PAGES ###

from requests import get
from bs4 import BeautifulSoup

"""We’ll scrape the first 4 pages of each year in the interval 2000-2017. 4 pages for each of the 18 
   years makes for a total of 72 pages. Each page has 50 movies, so we’ll scrape data for 3600 movies 
   at most. But not all the movies have a Metascore, so the number will be lower than that. Even so, 
   we are still very likely to get data for over 2000 movies."""

pages = [str(i) for i in range(1,5)] # Create a list called pages, and populate it with the strings corresponding to the first 4 pages.
years_url = [str(i) for i in range(2000,2018)] # Create a list called years_url and populate it with the strings corresponding to the years 2000-2017.

from time import sleep # Control the loop rate.  Will pause the execution for a specified amount of time. So our IP Address does not get banned. 
from random import randint # Varies the amount of wait time between requests. Creates a random integer within a specified interval. 
from time import time # Set a starting time
from IPython.core.display import clear_output # Clear -- View only the most recent request -- A bit more tidy when scraping multiple web pages. 

# Redeclaring the lists in which to store data
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0

# For every year in the interval 2000-2017
for year_url in years_url:

    # For every page in the interval 1-4
    for page in pages:

        # Make a get request
        response = get('http://www.imdb.com/search/title?release_date=' + year_url +
        '&sort=num_votes,desc&page=' + page, headers = {"Accept-Language": "en-US, en;q=0.5"}) # headers = {"Accept-Language": "en-US, en;q=0.5"} requests that we get all the scraped info in english even if we are over seas. 

        # Pause the loop
        sleep(randint(8,15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')
            break

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        # For every movie of these 50
        for container in mv_containers:
            # If the movie has a Metascore, then:
            if container.find('div', class_ = 'ratings-metascore') is not None:

                # Scrape the name
                name = container.h3.a.text
                names.append(name)

                # Scrape the year
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)

                # Scrape the IMDB rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                # Scrape the Metascore
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))

                # Scrape the number of votes
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))



### Examinging the Scraped Data
import pandas as pd
movie_ratings = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes
})
print(movie_ratings.info())
movie_ratings.head(10)

movie_ratings.to_csv('movie_ratings.csv')
