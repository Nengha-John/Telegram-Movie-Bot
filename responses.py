from datetime import datetime
import constants as keys
import requests as l

# movieURL = "https://api.themoviedb.org/3/search/movie?api_key=f66022942583a57f9df36a479bd83639&query="
# baseImgLink = "https://image.tmdb.org/t/p/w500/"
userInputs = {}
requests = {'q':'2'}

reportProblems = {}
def sampleResponse(inputText):
    userMessage = str(inputText).lower()

    if userMessage in {'hello', 'mambo','habari','hi','hey'}:
        return keys.welcomeText
    elif userMessage in {'/request','/report','@imdb','/report@dumbsterBot'}:
        return keys.textNotListed
    elif userMessage:
        uname = update.message.from_user['username']
        userInputs[uname]= userMessage
    elif userMessage in {'time','time?','what is the time?'}:
        now = datetime.now()
        dateTime = now.strftime("%H:%M:%S, %d/%m/%y")
        return "The time is " + str(dateTime)
    else:
        return keys.textNotListed
    
#fetch genre ids with their associated text value
genreURL = "https://api.themoviedb.org/3/genre/movie/list?api_key=f66022942583a57f9df36a479bd83639&language=en-US"
genreQuery = l.get(genreURL).json()
genreList = genreQuery['genres']
genres = {}
#create a dictionary with key value pairs of the genre id and associated genre name
for i in range(1,19):
    genres[genreList[i]['id']] = genreList[i]['name']
# for item in tryGenre:
#     if item in genres:
#         print(genres[item])
print("Here")