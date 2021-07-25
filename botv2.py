import constants as keys
from telegram.ext import *
import responses as R
import requests as r
from datetime import datetime as t
from telegram import ParseMode
print("Bot Started")


def startCommand(update,context):
    update.message.reply_text(keys.welcomeText,parse_mode=ParseMode.HTML)

def helpCommand(update,context):
    update.message.reply_text(keys.help,parse_mode=ParseMode.HTML)

def searchCommand(update,context):
    movieToSearch = str(update.message.text)
    movie = movieToSearch.replace("/search", "")
    if movie != "":
        captionText = processSearch(movie)[0]
        photo = processSearch(movie)[1]
        #send feedback to user
        context.bot.sendPhoto(chat_id = keys.groupId, photo = photo,caption = captionText,parse_mode = ParseMode.HTML)
    else:
        update.message.reply_text(keys.emptyFeedback,parse_mode=ParseMode.HTML) 

def processSearch(movieName): 
     #fetch movie details
    movieQuery = r.get(keys.movieSearchURL+movieName).json()
    print(len(movieQuery))
    for i in range(len(movieQuery)):
         print(i)
         #storing details in variables
         title = movieQuery['results'][0]['original_title']
         overview = movieQuery['results'][0]['overview']
         posterPath = movieQuery['results'][0]['poster_path']
         releaseDate = movieQuery['results'][0]['release_date']
         rating = movieQuery['results'][0]['vote_average']
         genresQuery = movieQuery['results'][0]['genre_ids']
         # movieId = movieQuery['results'][0]['id']
         # getTrailer = r.get()
         genreInMovie=""
         #extract the movie genre from the genre ids
         for genCode in genresQuery:
             if genCode in R.genres:
                 genreInMovie += "#"+R.genres[genCode]+ " "
         photo = keys.baseImgLink+posterPath
         #returned caption and poster image
         caption = "<b>Title:</b>  " + "<strong>"+str(title) +"</strong>"
         caption += "\n<b>Genres: </b>"+ str(genreInMovie) + "\n"
         caption += "\n<b>Ratings: </b>"+str(rating)
         caption += "\n<b>Release Date: </b>"+str(releaseDate)
         caption += "\n\n<b>Overview: </b>"+str(overview)
         captions = [caption,photo]
         return captions

def recommendCommand(update,context):
    movieToFindRecommend = str(update.message.text)
    movieR = movieToFindRecommend.replace("/recommend", "")
    if movieR != "":
        movieRecommend = r.get(keys.movieSearchURL+movieR).json()
        movieId = movieRecommend['results'][0]['movie_id']

def reportCommand(update,context):
    reportedProblem = str(update.message.text)
    problem = reportedProblem.replace("/report", "")
    if problem != "":
        username = update.message.from_user['username']
        writeReport(problem, username)
        R.reportProblems[username] = problem
        update.message.reply_text(keys.problemReported,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(keys.emptyFeedback,parse_mode=ParseMode.HTML)

def requestCommand(update,context):
    requestedMovie = str(update.message.text) 
    movieStr = requestedMovie.replace("/request","",1)
    list =['movie','series']
    if movieStr != "":
        if 'movie' or 'series' in movieStr.split():
            username = update.message.from_user['username']
            R.requests[username] = movieStr
            writeRequest(movieStr, username)
            update.message.reply_text(keys.requestSubmitted,parse_mode=ParseMode.HTML)
            print(f"User {update.message.from_user['username']} requested "+ movieStr)
            print(R.requests)
        else:
            update.message.reply_text(keys.kindNotStated,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(keys.emptyFeedback,parse_mode=ParseMode.HTML)

def writeRequest(reqq,uname):
    now = t.now()
    requestTime = now.strftime("%H:%M:%S, %d/%m/%y")
    try:
        file = open('/Users/proce/Desktop/Dumbster/DumbsterBot/request.txt','a') 
        file.write('Username: '+str(uname)+"\nRequest: "+str(reqq)+ "\nTime: "+ str(now))
        file.write('\n\n')
        file.flush()
        file.close()
    except IOError as error:
        print(error)

def writeReport(repo,uname):
    now = t.now()
    requestTime = now.strftime("%H:%M:%S, %d/%m/%y")
    try:
        file = open('/Users/proce/Desktop/Dumbster/DumbsterBot/reportproblems.txt','a') 
        file.write('Username: '+str(uname)+"\nReport: "+str(repo)+ "\nTime: "+ str(now))
        file.write('\n\n')
        file.flush()
        file.close()
    except IOError as error:
        print(error)

def handleMessage(update,context):
    text = str(update.message.text).lower()
    response = R.sampleResponse(text)
    update.message.reply_text(response,parse_mode=ParseMode.HTML)

def quoteCommand(update,context):
    quoteUrl = 'https://zenquotes.io/api/random/'
    quoteJson = r.get(quoteUrl).json()
    if quoteJson:
         quote = quoteJson[0]['q']
         author = quoteJson[0]['a']
         fQuote = '"'+ quote +'"' + ' ~<b>'+ author +'</b>' 
         update.message.reply_text(fQuote,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text('😢Samahani, ombi lako halijafanikiwa. Tafadhali jaribu tena.')

def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', startCommand))
    dp.add_handler(CommandHandler('help', helpCommand))
    dp.add_handler(CommandHandler("request", requestCommand))
    dp.add_handler(CommandHandler('report', reportCommand))
    dp.add_handler(CommandHandler('search', searchCommand))
    dp.add_handler(CommandHandler('quote',quoteCommand))
    dp.add_handler(MessageHandler(Filters.text,handleMessage))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
