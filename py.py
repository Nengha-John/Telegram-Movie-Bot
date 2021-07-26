import requests as l
# DONE get searched movie https://api.themoviedb.org/3/search/movie?api_key=f66022942583a57f9df36a479bd83639&query=
#  DONE get recommendeded movie https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=f66022942583a57f9df36a479bd83639&language=en-US&page=1
# DONE discover movies https://api.themoviedb.org/3/discover/movie?api_key=f66022942583a57f9df36a479bd83639&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate
# DONE get trending movies & tv https://api.themoviedb.org/3/trending/all/day?api_key=f66022942583a57f9df36a479bd83639
# DONE get searched tv shows https://api.themoviedb.org/3/search/tv?api_key=f66022942583a57f9df36a479bd83639&query=
#  DONE get tv show recommendations https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key=f66022942583a57f9df36a479bd83639&language=en-US&page=1
# DONE discover tv shows https://api.themoviedb.org/3/discover/tv?api_key=f66022942583a57f9df36a479bd83639&language=en-US&sort_by=popularity.desc&page=1&timezone=America%2FNew_York&include_null_first_air_dates=false&watch_region=us&with_watch_monetization_types=flatrate
# 

movieURL = "https://api.themoviedb.org/3/search/movie?api_key=f66022942583a57f9df36a479bd83639&query="
movieRecommendationURL = "https://api.themoviedb.org/3/movie/{}/recommendations?api_key=f66022942583a57f9df36a479bd83639&language=en-US"
baseImgLink = "https://image.tmdb.org/t/p/w500/"

movieRecommend = l.get(movieURL+movieR).json()
movieId = movieRecommend['results'][0]['id']
getRecommendedMovies = movieRecommendationURL.format(movieId)
recommendedMovies = l.get(getRecommendedMovies).json()
for i in range(len(recommendedMovies)):
    name = recommendedMovies['results'][i]['original_title']
    description = recommendedMovies['results'][i]['overview']
    rating = recommendedMovies['results'][i]['vote_average']
    date = recommendedMovies['results'][i]['release_date']
    print("Name: "+ str(name)+"\nRelease Date: " + str(date)+"\nRatings: "+ str(rating)+ "\nOverview: " + str(description)+"\n\n")