def recommend_movies(user_history, popular_movies, unpopular_movies):
    # TODO: implement the function to recommend movies.
    catalog_not_watched = set(popular_movies) - set(unpopular_movies) - set(user_history)
    
    return sorted(list(catalog_not_watched))



popular_movies = [1,3,2,4,5,10,10,10] 
user_history=  [1,2,3,15,16,14] 
unpopular_movies =  [5]

print(recommend_movies(user_history, popular_movies, unpopular_movies))