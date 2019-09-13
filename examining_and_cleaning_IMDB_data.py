### Examine and clean the scraped movie rating data from IMBD"


import pandas as pd
movie_ratings = pd.read_csv('movie_ratings.csv')
# col_names = movie_ratings.columns.tolist()
# print(col_names)
print(movie_ratings.info())
print(movie_ratings.head(10))

## Cleaning the Data ###
# Reorder the the Data 
movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
print(movie_ratings.head())

# Unique Values
print(movie_ratings['year'].unique()) # View unique years

# Select the numeric year and convert it to an integer 
movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
print(movie_ratings['year'].head(3)) # Check

# Min and Max Values (IMDB & Metascore) multiply IMDB rating by 10 to acheive normalization between the two variables. 
movie_ratings.describe().loc[['min', 'max'], ['imdb', 'metascore']] # Check for outliers

# Normalize IMDB and Metascore so they are on the same scale for graphing purposes 
movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
print(movie_ratings.head(3))

# Save Cleaned Dataset
movie_ratings.to_csv('movie_ratings_cleaned.csv')