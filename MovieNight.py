# %%
#Movie Night!
#Score of 75+
import pandas as pd
import numpy as np
import random

# %%
def MovieNight():
    
    movies = pd.read_csv(r"C:\Users\Dylan z4\OneDrive\Documents\MoviesOnStreamingPlatforms.csv")
    watched_movies = pd.read_csv(r"C:\Users\Dylan z4\OneDrive\Documents\WatchedMovies.csv")
    movie_len = len(movies.columns)
    print(movie_len)
    if movie_len >=11:
        movies = movies.drop(['Unnamed: 0'],axis=1)
        movies['Rotten Tomatoes'] = movies['Rotten Tomatoes'].str[:-4]
        movies['x'] = pd.to_numeric(movies['Rotten Tomatoes'], errors='coerce')
        movies = movies.dropna(subset=['x'])

        movies['Rotten Tomatoes'].fillna(0)
        movies['Rotten Tomatoes'] = movies['Rotten Tomatoes'].astype('int')
        top_movies = movies[movies['Rotten Tomatoes']>74]
        top_movies = top_movies.drop(['Type','x'],axis=1)
    else:
        top_movies = movies

    # %%
    selection = top_movies.sample()
    print(selection)

    top_movies = top_movies.drop(selection.index)

    top_movies.to_csv(r"C:\Users\Dylan z4\OneDrive\Documents\MoviesOnStreamingPlatformsCopy.csv",index=False)
    selection.to_csv(r"C:\Users\Dylan z4\OneDrive\Documents\WatchedMovies.csv",index=False,mode='a',header=False)

MovieNight()

