# Recommendations with MovieTweetings
# Getting to Know The Data:
  Throughout this recommendation project, i will be working with the MovieTweetings Data
  MovieTweetings is a dataset consisting of ratings on movies that were contained in well-structured
  tweets on Twitter. This dataset is the result of research conducted by [Simon  Dooms] (http://scholar.google.be/citations?user=owaD8qkAAAAJ) 
  (Ghent University, Belgium) and has been presented on the CrowdRec 2013 workshop which is co-located with the ACM RecSys 2013 conference. 
  Please cite the corresponding paper if you make use of this dataset. The presented slides can be found [on slideshare] 
  (http://www.slideshare.net/simondooms/movie-tweetings-a-movie-rating-dataset-collected-from-twitter).
  
# Data Cleaning:
  Next, we need to pull some additional relevant information out of the existing columns.
  For each of the datasets ( movies, reviews ), there are a couple of cleaning steps we need to take care of:
  
  - Pull the date from the title and create new column
  - Dummy the date column with 1's and 0's for each century of a movie (1800's, 1900's, and 2000's)
  - Dummy column the genre with 1's and 0's for each genre
  - Create a date out of timestamp
  
 # Most Popular Recommendation:
  Now that i have created the necessary columns that i will be using throughout the rest of the project on creating recommendations, 
  let's get started with the first of our recommendations, Most Popular Recommendation.
  
  How To Find The Most Popular Movies:
  - A movie with the highest average rating is considered best.
  - With ties, movies that have more ratings are better.
  - A movie must have a minimum of 5 ratings to be considered among the best movies.
  - If movies are tied in their average rating and number of ratings, the ranking is determined by the movie that is the most recent rating.
  
  # Collaborative Filtering:
  One of the most popular methods for making recommendations is collaborative filtering. In collaborative filtering, you are using the collaboration of user-item recommendations
  to assist in making new recommendations, in this project i gonna be working on performing neighborhood-based collaborative filtering.
  
  How To perform collaborative Filtering:
  - Measures of Similarity ( euclidien distance )
  - User-Item Matrix ( user id on rows and movies on columns )

 
