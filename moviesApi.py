# fetch movie details DONE
# movie searches DONE
# movie details DONE
# movie discover DONE
# recommendations DONE

import requests as r
import constants as keys
print("Testing Intiated....")

#Movie functions
def getMovieDetails(movieResult,i=0):
    #storing details in variables
    movieId = movieResult['results'][i]['id']
    title = movieResult['results'][i]['original_title']
    overview = movieResult['results'][i]['overview']
    posterPath = keys.baseImgLink + movieResult['results'][i]['poster_path']
    imagePath = keys.baseImgLink + movieResult['results'][i]['backdrop_path']
    releaseDate = movieResult['results'][i]['release_date']
    rating = movieResult['results'][i]['vote_average']
    genresInMovie = movieResult['results'][i]['genre_ids']
    genreList = []
    #extract the movie genre from the genre ids
    for genCode in genresInMovie:
        if genCode in keys.genreIds:
            genreList.append(keys.genreIds[genCode])
    
    movieDetails = {'id': movieId,'title':title,'description': overview, 'poster':posterPath,'images': imagePath,'release': releaseDate,'rating': rating,'genres': genreList}
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
    photo = movieD['poster']
    captions = [caption,photo]
    return captions

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
        name = recommendedMovies['results'][i]['original_title']
        description = recommendedMovies['results'][i]['overview']
        rating = recommendedMovies['results'][i]['vote_average']
        date = recommendedMovies['results'][i]['release_date']
        poster = keys.baseImgLink + recommendedMovies['results'][i]['poster_path']
        Rmovie = {'title': name,'description': description,'rating':rating,'release': date,'poster':poster}
        recommendationsM.append(Rmovie)
    return recommendationsM

def discoverMovies():
    movieQuery = r.get(keys.movieDiscoverURL).json()
    Dmovies = []
    for j in range(len(movieQuery['results'])):
        movieD = getMovieDetails(movieQuery,j)
        Dmovies.append(movieD)
 
def trendingMovies():
    movieQuery = r.get(keys.movieTrendingURL).json()
    Tmovies = []
    for k in range(len(movieQuery['results'])):
        movieT = getMovieDetails(movieQuery,k)
        Tmovies.append(movieT)





#shows functions
def getShowDetails(showResult,j=0):
    #storing results in variable
    showId = showResult['results'][j]['id']
    title = showResult['results'][j]['name']
    overview = showResult['results'][j]['overview']
    posterPath = keys.baseImgLink + str(showResult['results'][j]['poster_path'])
    imagePath = keys.baseImgLink + showResult['results'][j]['backdrop_path']
    releaseDate = showResult['results'][j]['first_air_date']
    rating = showResult['results'][j]['vote_average']
    genresInShow = showResult['results'][j]['genre_ids']
    genreList = []
    #extract the movie genre from the genre ids
    for genCode in genresInShow:
        if genCode in keys.genreIds:
            genreList.append(keys.genreIds[genCode])
    showDetails = {'id': showId,'title':title,'description': overview, 'poster':posterPath,'images': imagePath,'release': releaseDate,'rating': rating,'genres': genreList}
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
    photo = showD['poster']
    captions = [caption,photo]
    return captions

def searchShow(showName):
    #fetch show details
    showQuery = r.get(keys.showSearchURL+showName).json()
    detailedShow = getShowDetails(showQuery)
    cap = generateShowCaption(detailedShow)
    print(detailedShow)
    print(cap)

def getRecommendedShows(showR):
    showQuery = r.get(keys.showSearchURL+showR).json()
    showRid = showQuery['results'][0]['id']
    print(showRid)
    recommendURL = keys.showRecommendationURL.format(showRid)
    recommendedShows = r.get(recommendURL).json()
    Srecommendations = []
    for i in range(len(recommendedShows)):
        name = recommendedShows['results'][i]['name']
        description = recommendedShows['results'][i]['overview']
        rating = recommendedShows['results'][i]['vote_average']
        date = recommendedShows['results'][i]['first_air_date']
        poster = keys.baseImgLink + recommendedShows['results'][i]['poster_path']
        Rmovie = {'title': name,'description': description,'rating':rating,'release': date,'poster':poster}
        Srecommendations.append(Rmovie)
    return Srecommendations


def discoverShows():
    showQuery = r.get(keys.showDiscoverURL).json()
    Dshows = []
    for j in range(len(showQuery['results'])):
        showD = getShowDetails(showQuery,j)
        Dshows.append(showD)
    return Dshows

def trendingShows():
    showQuery = r.get(keys.showTrendingURL).json()
    Tshows = []
    print(len(showQuery['results']))
    for j in range(len(showQuery['results'])):
        showT = getShowDetails(showQuery,j)
        Tshows.append(showT)
    for l in Tshows:
        print(l)
        print("\n\n")



