import numpy as np
import pandas as pd


def movies_names(movies_ids):
    """Take in movie ids and return movies names"""
    movies_names = list(movies[movies["Movie ID"].isin(movies_ids)]["Movie Title"])
    return movies_names


def create_ranked_df(movies, reviews):
    """Take in the movies and reviews dateset and return the ranked movies"""
    movie_ratings = reviews.groupby("Movie ID")["Rating"]
    avg_ratings = movie_ratings.mean() 
    num_ratings = movie_ratings.count()
    last_rating = pd.DataFrame(reviews.groupby("Movie ID").max()["date_time"])
    last_rating.columns = ["last_rating"]
    
    ratings_count_df = pd.DataFrame({"avg_ratings":avg_ratings, 'num_ratings':num_ratings})
    ratings_count_df = ratings_count_df.join(last_rating)
    
    movies_rec = movies.set_index("Movie ID").join(ratings_count_df)
    ranked_movies = movies_rec.sort_values(["avg_ratings", "num_ratings", "last_rating"], ascending = False)
    ranked_movies = ranked_movies[ranked_movies["num_ratings"] > 4]
    return ranked_movies

def popular_recommendations(user_id, n_top, ranked_movies):
    top_movies = list(ranked_movies['movie'][:n_top])
    return top_movies