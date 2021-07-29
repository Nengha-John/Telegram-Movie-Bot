# fetch movie details DONE
# movie searches DONE
# movie details DONE
# movie discover DONE
# recommendations DONE
#movie trailers

import requests as r
import constants as keys
print("Testing Intiated....")

#Movie functions
def getMovieTrailer(movieId):
    trailerQuery = r.get(keys.movieTrailerURL.format(movieId)).json()
    trailerKey = trailerQuery['results'][0]['key']
    trailerPath = keys.baseYoutubeLink + trailerKey
    return trailerPath

def getMovieDetails(movieResult,i=0):
    #storing details in variables
    movieId = movieResult['results'][i]['id']
    title = movieResult['results'][i]['original_title']
    overview = movieResult['results'][i]['overview']
    posterPath = keys.baseImgLink + movieResult['results'][i]['poster_path']
    imagePath = keys.baseImgLink + str(movieResult['results'][i]['backdrop_path'])
    trailer = getMovieTrailer(movieId)
    releaseDate = movieResult['results'][i]['release_date']
    rating = movieResult['results'][i]['vote_average']
    genresInMovie = movieResult['results'][i]['genre_ids']
    genreList = []
    #extract the movie genre from the genre ids
    for genCode in genresInMovie:
        if genCode in keys.genreIds:
            genreList.append(keys.genreIds[genCode])
    
    movieDetails = {'id': movieId,'title':title,'description': overview,'trailer': trailer, 'poster':posterPath,'images': imagePath,'release': releaseDate,'rating': rating,'genres': genreList}
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


#process the searching of a movie
def searchMovie(movieName): 
    #fetch movie details
    movieQuery = r.get(keys.movieSearchURL+movieName).json()
    detailedMovie = getMovieDetails(movieQuery)
    return detailedMovie

def getRecommendedMovies(movieR):
    movieQuery = r.get(keys.movieSearchURL+movieR).json()
    movieRid = movieQuery['results'][0]['id']
    recommendURL = keys.movieRecommendationURL.format(movieRid)
    recommendedMovies = r.get(recommendURL).json()
    recommendationsM = []
    for i in range(len(recommendedMovies)):
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

getShowTrailer(86546)
def getShowDetails(showResult,j=0):
    if len(showResult['results']) != 0:
        #storing results in variable
        showId = showResult['results'][j]['id']
        title = showResult['results'][j]['name']
        overview = showResult['results'][j]['overview']
        posterPath = keys.baseImgLink + str(showResult['results'][j]['poster_path'])
        imagePath = keys.baseImgLink + str(showResult['results'][j]['backdrop_path'])
        trailerPath = getShowTrailer(showId)
        releaseDate = showResult['results'][j]['first_air_date']
        rating = showResult['results'][j]['vote_average']
        genresInShow = showResult['results'][j]['genre_ids']
        genreList = []
        #extract the movie genre from the genre ids
        for genCode in genresInShow:
            if genCode in keys.genreIds:
                genreList.append(keys.genreIds[genCode])
        showDetails = {'id': showId,'title':title,'description': overview, 'trailer': trailerPath, 'poster':posterPath,'images': imagePath,'release': releaseDate,'rating': rating,'genres': genreList}
    return showDetails 

def generateShowCaption(showD):
    #returned caption and poster image
    caption = "<b>Title:</b>  " + "<strong>"+str(showD['title']) +"</strong>"
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
    detailedShow = getShowDetails(showQuery)
    cap = generateShowCaption(detailedShow)
    return detailedShow

def getRecommendedShows(showR):
    showQuery = r.get(keys.showSearchURL+showR).json()
    if len(showQuery['results']) != 0:
         showRid = showQuery['results'][0]['id']
         recommendURL = keys.showRecommendationURL.format(showRid)
         recommendedShows = r.get(recommendURL).json()
         Srecommendations = []
         for i in range(len(recommendedShows)):
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





