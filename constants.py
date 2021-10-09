import requests as r
import os
## *********************** ##
#Congif env variables
## *********************** ##


#Telegram Bot Api 
#Get it from Bot Father @BotFather
BOT_API_KEY = os.environ.get('BOT_API_KEY')

#TMDB Api Key
#Get it from developer.tmdb.org
API_KEY = os.environ.get('TMDB_API_KEY')

#Telegram Group IDs
groupId = os.environ.get('MAIN_GROUP_ID')  #Movies group
requestGroupId = os.environ.get('REQUESTS_GROUP_ID') #Requests Group
channelID = os.environ.get('SERIES_CHANNEL_ID')  #Series Channel
playgroundId = os.environ.get('TESTING_GROUP_ID')  #Testing group
admin = os.environ.get('ADMIN_CHAT_ID')   #Admin Chat Id

#movie api links
movieSearchURL = "https://api.themoviedb.org/3/search/movie?api_key=%s&query="%API_KEY
movieRecommendationURL = "https://api.themoviedb.org/3/movie/{}/recommendations?api_key=%s&language=en-US&page=1"%API_KEY
movieDiscoverURL = 'https://api.themoviedb.org/3/discover/movie?api_key=%s&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate'%API_KEY
movieTrendingURL = "https://api.themoviedb.org/3/trending/movie/week?api_key=%s&page=1"%API_KEY
movieTrailerURL = "https://api.themoviedb.org/3/movie/{}/videos?api_key=%s&language=en-US"%API_KEY
movieUpcomingURL = "https://api.themoviedb.org/3/movie/upcoming?api_key=%s&language=en-US"%API_KEY

#show api links
showSearchURL ='https://api.themoviedb.org/3/search/tv?api_key=%s&query='%API_KEY
showRecommendationURL = "https://api.themoviedb.org/3/tv/{}/recommendations?api_key=%s&language=en-US&page=1"%API_KEY
showDiscoverURL = "https://api.themoviedb.org/3/discover/tv?api_key=%s&language=en-US&sort_by=popularity.desc&page=1&timezone=America&include_null_first_air_dates=false&with_watch_monetization_types=flatrate"%API_KEY
showTrendingURL = "https://api.themoviedb.org/3/trending/tv/week?api_key=%s&page=1"%API_KEY
showTrailerURL = "https://api.themoviedb.org/3/tv/{}/videos?api_key=%s&language=en-US"%API_KEY


#get poster image from moviesdb
baseImgLink = "https://image.tmdb.org/t/p/w500/"
baseYoutubeLink = "https://www.youtube.com/watch?v="

#fetch genre ids with their associated text value
genreURL = "https://api.themoviedb.org/3/genre/movie/list?api_key=%s&language=en-US"%API_KEY
genreIdQuery = r.get(genreURL).json()
genreIdList = genreIdQuery['genre_ids']

#create a dictionary with key value pairs of the genre id and associated genre name
genreIds = {}
for i in range(1,19):
    genreIds[genreIdList[i]['id']] = genreIdList[i]['name']



