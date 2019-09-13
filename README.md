
# webscraping_multiple_pages
 

1.
First, we’ll scrape the first 4 pages of each year in the interval 2000-2017. 
4 pages for each of the 18 years makes for a total of 72 pages. Each page has 
50 movies, so we’ll scrape data for 3600 movies at most. But not all the movies 
have a Metascore, so the number will be lower than that. Even so, we are still 
very likely to get data for over 2000 movies.

Files to use:
webscraping_multiple_pages.py

Creates file:
moive_ratings.csv


2.
Second, we will examine and clean the scraped IMDB data

Files to use:
moive_ratings.csv
examining_and_cleaning_IMDB_data.py

Creates File:
moive_ratings_cleaned.csv


3. 
Third, we will create visualizations to understand our data sturcture and 
distribution.

Files to use:
moive_ratings_cleaned.csv
plotting_and_analysis_imdb.py