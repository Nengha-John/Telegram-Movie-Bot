import constants as keys
import moviesApi as api
from telegram.ext import *
import telegram
import responses as R
import requests as r
from telegram import ParseMode
from datetime import datetime as t
import datetime as T
import time
print("Bot Started")


def startCommand(update,context):
    update.message.reply_text(R.welcomeText,parse_mode=ParseMode.HTML)

def helpCommand(update,context):
    update.message.reply_text(R.help,parse_mode=ParseMode.HTML)



#search movie command
def searchMCommand(update,context):
    movieToSearch = str(update.message.text)
    movie = movieToSearch.replace("/searchM", "")
    if movie != "":
        print('\n\n')
        print(">>Searching Movie <<" + movie.upper() +" >>")
        movieResult = api.searchMovie(movie)
        if len(movieResult) != 0:
             print('>>Movie Found..\n>>Generating Movie Details..')
             caption = api.generateMovieCaption(movieResult)
             trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(movieResult))]])
             #send feedback to user
             context.bot.sendPhoto(chat_id = keys.groupId, photo = movieResult['poster'],caption = caption,parse_mode = ParseMode.HTML,reply_markup = trailer)
             print("<< Movie Sent.")
             print('\n\n')
        else:
             print(">>Movie not Found")
             update.message.reply_text(R.notFound,parse_mode=ParseMode.HTML) 
    else:
        update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 

#search show command
def searchSCommand(update,context):
    showToSearch = str(update.message.text)
    show = showToSearch.replace("/searchS", "")
    if show != "":
        print('\n\n')
        print(">>Searching Show <<< "+show.upper()+" >>>")
        showResult = api.searchShow(show)
        if len(showResult) != 0:
             print(">>Show Found.. \n>> Generating Show Details..")
             caption = api.generateShowCaption(showResult)
             trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(showResult))]])
             #send feedback to user
             context.bot.sendPhoto(chat_id = keys.groupId, photo = showResult['poster'],caption = caption,parse_mode = ParseMode.HTML,reply_markup = trailer)
             print("<< Show sent.")
             print('\n\n')
        else:
             update.message.reply_text(R.notFound,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 



#get movie recommendations based on a given movie
def recommendMCommand(update,context):
    movieToFindRecommend = str(update.message.text)
    movieR = movieToFindRecommend.replace("/recommendM", "")
    if movieR != "":
        print('\n\n')
        print(">> Fetching Recommendations <<< "+movieR.upper()+" >>>")
        recommendedMovies = api.getRecommendedMovies(movieR)
        if len(recommendedMovies) != 0:
            print(">> Recommendations Found: "+str(len(recommendedMovies)))
            print(">>Working on Recommendations")
            for i in range(len(recommendedMovies)):
                caption = api.generateMovieCaption(recommendedMovies[i])
                trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(recommendedMovies[i]))]])
                context.bot.sendPhoto(chat_id = keys.groupId, photo = recommendedMovies[i]['poster'],caption = caption,parse_mode = ParseMode.HTML,reply_markup = trailer)
                print(">> Sending Recommendation  "+ str(i + 1))
                time.sleep(2)
            print('<< Total Recommendations Sent: ' + str(len(recommendedMovies)))
            print('\n\n')
        else:
             update.message.reply_text(R.notFound,parse_mode=ParseMode.HTML)
    else:
         update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 

#get show recommendations based on a given show
def recommendSCommand(update,context):
    showToFindRecommend = str(update.message.text)
    showR = showToFindRecommend.replace('/recommendS',"")
    if showR != "":
        print('\n\n')
        print(">> Fetching Recommendations <<< "+showR.upper()+" >>>")
        recommendedShows = api.getRecommendedShows(showR)
        if len(recommendedShows) != 0:
            print(">> Recommendations Found: "+ str(len(recommendedShows)))
            print(">>Working on Recommendations...")
            for i in range(len(recommendedShows)):
                caption = api.generateShowCaption(recommendedShows[i])
                trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(recommendedShows[i]))]])
                context.bot.sendPhoto(chat_id = keys.groupId, photo = recommendedShows[i]['poster'],caption = caption, reply_markup = trailer, parse_mode = ParseMode.HTML)
                print(">> Sending Recommendation "+ str(i + 1))
                time.sleep(2)
            print('<< Total Recommendations sent: ' + str(len(recommendedShows)))
            print('\n\n')
        else:
            update.message.reply_text(R.notFound,parse_mode=ParseMode.HTML) 
    else:
         update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 



#discover movies
def discoverMCommand(update,context):
    print('\n\n')
    print(">> Discovering Movies")
    dMovies = api.discoverMovies()
    print(">> Movies Discovered: "+ str(len(dMovies)))
    for i in range(len(dMovies)):
        caption = api.generateMovieCaption(dMovies[i])
        trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(dMovies[i]))]])
        context.bot.sendPhoto(chat_id = keys.groupId, photo = dMovies[i]['poster'],caption = caption, reply_markup = trailer, parse_mode = ParseMode.HTML)
        print(">> Sending Discovered Movie: "+ str(i + 1))
        time.sleep(2)
    print("<< Total Movies Sent " + str(len(dMovies)))
    print('\n\n')

#discover shows
def discoverSCommand(update,context):
    print('\n\n')
    print(">> Discovering Shows")
    dShows = api.discoverShows()
    print(">> Discovered  Shows: "+ str(len(dShows)))
    for i in range(len(dShows)):
        caption = api.generateShowCaption(dShows[i])
        trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(dShows[i]))]])
        context.bot.sendPhoto(chat_id = keys.groupId, photo = dShows[i]['poster'],caption = caption, reply_markup = trailer, parse_mode = ParseMode.HTML)
        print(">> Sending Discovered Movie: "+ str(i + 1))
        time.sleep(2)
    print("<< Total Shows Sent: " + str(len(dShows)))
    print('\n\n')




#get trending movies
def trendingMCommand(update,context):
    print('\n\n')
    print(">> Fetching Trending Movies")
    tMovies = api.trendingMovies()
    print(">> Trending Movies Found "+ str(len(tMovies)))
    for i in range(len(tMovies)):
        caption = api.generateShowCaption(tMovies[i])
        trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(showResult))]])
        context.bot.sendPhoto(chat_id = keys.groupId, photo = tMovies[i]['poster'],caption = caption, reply_markup = trailer,parse_mode = ParseMode.HTML)
        print(">> Sending trending Movie: "+ str(i + 1))
        time.sleep(2)
    print("<< Total Movies Sent " + str(len(tMovies)))
    print('\n\n')

#get trending shows
def trendingSCommand(update,context):
    print('\n\n')
    print(">> Fetching Trending Shows")
    tShows = api.trendingShows()
    print(">> Trending Shows Found: "+ str(len(tShows)))
    for i in range(len(tShows)):
        caption = api.generateShowCaption(tShows[i])
        trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(tShows[i]))]])
        context.bot.sendPhoto(chat_id = keys.groupId, photo = tShows[i]['poster'], caption = caption, reply_markup = trailer,parse_mode = ParseMode.HTML)
        print(">> Sending Trending Show: "+ str(i + 1))
        time.sleep(2)
    print("<< Total Shows Sent: " + str(len(tShows)))
    print('\n\n')




def requestCommand(update,context):
    requestedMovie = str(update.message.text) 
    movieStr = requestedMovie.replace("/request","",1)
    list =['movie','series']
    if movieStr != "":
        if 'movie' or 'series' in movieStr.split():
            username = update.message.from_user['username']
            print('\n\n')
            print(">> Requested movie : "+ movieStr.upper())
            writeRequest(movieStr, username)
            update.message.reply_text(R.requestSubmitted,parse_mode=ParseMode.HTML)
        else:
            update.message.reply_text(R.kindNotStated,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML)

def writeRequest(reqq,uname):
    now = t.now()
    requestTime = now.strftime("%H:%M:%S, %d/%m/%y")
    try:
        file = open('/Users/proce/Desktop/Dumbster/DumbsterBot/request.txt','a') 
        file.write('Username: '+str(uname)+"\nRequest: "+str(reqq)+ "\nTime: "+ str(now))
        file.write('\n\n')
        file.flush()
        file.close()
        print("<< Write successfull")
        print('\n\n')
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
    print(f"Error {context.error}")
    
def weeklyTrending(context:CallbackContext):
        trendingMCommand()
        sleep(10)
        trendingSCommand()


def main():
    updater = Updater(keys.BOT_API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', startCommand))
    dp.add_handler(CommandHandler('help', helpCommand))
    dp.add_handler(CommandHandler("request", requestCommand))

    # Handle search commands
    dp.add_handler(CommandHandler('searchM', searchMCommand))
    dp.add_handler(CommandHandler('searchS', searchSCommand))

    #Handle recommendations
    dp.add_handler(CommandHandler('recommendM', recommendMCommand))
    dp.add_handler(CommandHandler('recommendS', recommendSCommand))
    
    #Handle discover commands
    dp.add_handler(CommandHandler('discoverM', discoverMCommand))
    dp.add_handler(CommandHandler('discoverS', discoverSCommand))

    #Handle trending commands
    dp.add_handler(CommandHandler('trendingM',trendingMCommand))
    dp.add_handler(CommandHandler('trendingS', trendingSCommand))

    #Testing scheduled messaging
    j = updater.job_queue
    j.run_daily(weeklyTrending,time= T.time(8,00), days=(0))
    dp.add_handler(CommandHandler('quote',quoteCommand))
    dp.add_handler(MessageHandler(Filters.text,handleMessage))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
