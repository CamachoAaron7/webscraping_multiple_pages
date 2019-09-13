
""""""

import pandas as pd
movie_ratings = pd.read_csv('movie_ratings_cleaned.csv')
# col_names = movie_ratings.columns.tolist()
# print(col_names)
print(movie_ratings.info())
print(movie_ratings.head(10))


### Plot 
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes
ax1.hist(movie_ratings['imdb'], bins = 10, range = (0,10)) # bin range = 1
ax1.set_title('IMDB rating')
ax1.set_xlabel('Rating', fontsize = 14)
ax1.set_ylabel('# of ratings', fontsize = 14)
ax2.hist(movie_ratings['metascore'], bins = 10, range = (0,100)) # bin range = 10
ax2.set_title('Metascore')
ax2.set_xlabel('Rating', fontsize = 14)
ax2.set_ylabel('# of ratings', fontsize = 14)
ax3.hist(movie_ratings['n_imdb'], bins = 10, range = (0,100), histtype = 'step')
ax3.hist(movie_ratings['metascore'], bins = 10, range = (0,100), histtype = 'step')
ax3.legend(loc = 'upper left')
ax3.set_title('The Two Normalized Distributions')
ax3.set_xlabel('Rating', fontsize = 14)
ax3.set_ylabel('# of ratings', fontsize = 14)
for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
plt.show()


""" 
IMDB Histogram: Shows that the majority of ratings are between 6 and 8.  
				There are few movies with a rating higher than 8 and 
				lower than 4.  We can deduce that there are very few very 
				bad and few very good movies. However we can see that the 
				distribution is skewed to the right (See below for possible
				reason). 

Metascore Histogram: Resembles a bell curve/normal distribution.  
					 The majoriy of ratings lay approximatley at
					 50.  From that peak the scores gradually decrease
					 at both ends. Again, we can deduce that there are few
					 very bad and few very good movies from this distribution.


Skewness of IMDB Histogram: Why is this histogram skewed.  One possible reason/
 							hypothesis is that people in general think in a binary
 							sense. Either the movie was good or the movie was bad. 
 							When a movie is good it can be considered close to if not
 							a 10 rating. Also, when the movie is good people are more 
 							leave a rating. However, when a movie is bad a small rating
 							is given and/or people are less likely to rate the movie. 
 							Worth looking into it in another study.   """