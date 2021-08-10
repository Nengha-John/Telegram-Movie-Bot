# fetch movie details DONE
# movie searches DONE
# movie details DONE
# movie discover DONE
# recommendations DONE
#movie trailers

import requests as r
import constants as keys
import time
print("Testing Intiated....")

#Movie functions
def getMovieTrailer(movieId):
    trailerQuery = r.get(keys.movieTrailerURL.format(movieId)).json()
    trailerPath =''
    if len(trailerQuery['results']) != 0:
         trailerKey = trailerQuery['results'][0]['key']
         trailerPath = keys.baseYoutubeLink + trailerKey
    else:
         trailerPath = "https://www.youtube.com/results?search_query="
    return trailerPath

def getMovieDetails(movieResult,i=0):
    #storing details in dictionaries
    movie = {}
    for key,value in movieResult['results'][i].items():
        movie[key] = value
    
    if movie['poster_path'] is None:
        posterPath = open('DumbsterBot/404.png','rb')
    else:
        posterPath = keys.baseImgLink + str(movie['poster_path'])
    genreList = []
    #extract the movie genre from the genre ids
    for genCode in movie['genre_ids']:
        if genCode in keys.genreIds:
            genreList.append(keys.genreIds[genCode])
    trailer = getMovieTrailer(movie['id'])
    movieDetails = {'id': movie['id'],'title':movie['original_title'],'description': movie['overview'],'trailer': trailer, 'poster':posterPath,'images': movie['backdrop_path'],'release': movie['release_date'],'rating': movie['vote_average'],'genres': genreList}
    return movieDetails 

def generateMovieCaption(movieD):
    #returned caption and poster image
    caption = "<b>Title:</b>  " + "<strong>"+str(movieD['title']) +"</strong>"
    extGenre = movieD['genres']
    capGenre = ""
    for item in extGenre:
        capGenre += "#" + item + " "
    caption += "\n<b>Genres: </b>"+ str(capGenre) + "\n"
    caption += "\n<b>Ratings: </b>"+str(movieD['rating'])
    caption += "\n<b>Release Date: </b>"+str(movieD['release'])
    caption += "\n\n<b>Overview: </b>"+str(movieD['description'])
    return caption

def getTrailerLink(Dmovie):
    return Dmovie['trailer']

def getPoster(link):
       posterPath = keys.baseImgLink + str(link)
       return posterPath

#process the searching of a movie
def searchMovie(movieName): 
    #fetch movie details
    movieQuery = r.get(keys.movieSearchURL+movieName).json()
    Movies = []
    for i in range(len(movieQuery['results'])):
         detailedMovie = getMovieDetails(movieQuery,i)
         Movies.append(detailedMovie)
    return Movies

def getRecommendedMovies(movieR):
    movieQuery = r.get(keys.movieSearchURL+movieR).json()
    movieRid = movieQuery['results'][0]['id']
    recommendURL = keys.movieRecommendationURL.format(movieRid)
    recommendedMovies = r.get(recommendURL).json()
    recommendationsM = []
    for i in range(len(recommendedMovies['results'])):
        Rmovie = getMovieDetails(recommendedMovies,i)
        recommendationsM.append(Rmovie)
    return recommendationsM

def discoverMovies():
    movieQuery = r.get(keys.movieDiscoverURL).json()
    Dmovies = []
    for j in range(len(movieQuery['results'])):
        movieD = getMovieDetails(movieQuery,j)
        Dmovies.append(movieD)
    return Dmovies
 
def trendingMovies():
    movieQuery = r.get(keys.movieTrendingURL).json()
    Tmovies = []
    for k in range(len(movieQuery['results'])):
        movieT = getMovieDetails(movieQuery,k)
        Tmovies.append(movieT)
    return Tmovies

def upcomingMovies():
    movieQuery = r.get(keys.movieUpcomingURL).json()
    Umovies = []
    for k in range(len(movieQuery['results'])):
        movieU = getMovieDetails(movieQuery,k)
        Umovies.append(movieU)
    return Umovies


#shows functions
def getShowTrailer(showId):
    trailerQuery = r.get(keys.showTrailerURL.format(showId)).json()
    trailerPath = ""
    if len(trailerQuery['results']) != 0:
        trailerKey = trailerQuery['results'][0]['key']
        trailerPath = keys.baseYoutubeLink + trailerKey
    else:
        trailerPath = "https://www.youtube.com/results?search_query=" 
    return trailerPath


def getShowDetails(showResult,j=0):
    if len(showResult['results']) != 0:
        #storing details in dictionaries
        show = {}
        for key,value in showResult['results'][j].items():
            show[key] = value
    
        if show['poster_path'] is None:
            posterPath = open('DumbsterBot/404.png','rb')
        else:
            posterPath = keys.baseImgLink + str(show['poster_path'])
        genreList = []
        #extract the movie genre from the genre ids
        for genCode in show['genre_ids']:
            if genCode in keys.genreIds:
                genreList.append(keys.genreIds[genCode])
        trailerPath = getShowTrailer(show['id'])
        imagePath = keys.baseImgLink + str(showResult['results'][j]['backdrop_path'])
        showDetails = {'id': show['id'],'title':show['name'],'description': show['overview'], 'trailer': trailerPath, 'poster':posterPath,'images': imagePath,'release': show['first_air_date'],'rating': show['vote_average'],'genres': genreList}
    return showDetails 

def generateShowCaption(showD):
    #returned caption and poster image
    caption = "<b>Title:</b>  " + "<strong>"+str(showD['title']) + "</strong>"
    extGenre = showD['genres']
    capGenre = ""
    for item in extGenre:
        capGenre += "#" + item + " "
    caption += "\n<b>Genres: </b>"+ str(capGenre) + "\n"
    caption += "\n<b>Ratings: </b>"+str(showD['rating'])
    caption += "\n<b>Release Date: </b>"+str(showD['release'])
    caption += "\n\n<b>Overview: </b>"+str(showD['description'])
    return caption

def searchShow(showName):
    #fetch show details
    showQuery = r.get(keys.showSearchURL+showName).json()
    Shows = []
    for i in range(len(showQuery['results'])):
         detailedShow = getShowDetails(showQuery,i)
         Shows.append(detailedShow)
    return Shows

def getRecommendedShows(showR):
    showQuery = r.get(keys.showSearchURL+showR).json()
    if len(showQuery['results']) != 0:
         showRid = showQuery['results'][0]['id']
         recommendURL = keys.showRecommendationURL.format(showRid)
         recommendedShows = r.get(recommendURL).json()
         Srecommendations = []
         for i in range(len(recommendedShows['results'])):
             Rshow = getShowDetails(recommendedShows,i)
             Srecommendations.append(Rshow)
    else:
        Srecommendations = []
    return Srecommendations

def discoverShows():
    showQuery = r.get(keys.showDiscoverURL).json()
    Dshows = []
    if len(showQuery['results']) != 0:
        for j in range(len(showQuery['results'])):
            showD = getShowDetails(showQuery,j)
            Dshows.append(showD)
    return Dshows

def trendingShows():
    showQuery = r.get(keys.showTrendingURL).json()
    Tshows = []
    for j in range(len(showQuery['results'])):
        showT = getShowDetails(showQuery,j)
        Tshows.append(showT)
    return Tshows




