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
from bs4 import BeautifulSoup 
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
        msg = update.message.reply_text("Searching Movie...")
        movieResult = api.searchMovie(movie)
        time.sleep(2)
        if len(movieResult) != 0:
             msg.edit_text( str(len(movieResult)) + " Movie(s) Found")
             print('>>Movie Found..\n>>Generating Movie Details..')
             time.sleep(2)
             for i in range(len(movieResult)):
                  caption = api.generateMovieCaption(movieResult[i])
                  trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(movieResult[i]))]])
                  #send feedback to user
                  context.bot.sendPhoto(chat_id = keys.groupId, photo = movieResult[i]['poster'],caption = caption,parse_mode = ParseMode.HTML,reply_markup = trailer)
                  time.sleep(2)
             print("<< Movie Sent.")
             print('\n\n')
        else:
             print(">>Movie not Found")
             msg.edit_text(R.notFound,parse_mode=ParseMode.HTML) 
    else:
        update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 

#search show command
def searchSCommand(update,context):
    showToSearch = str(update.message.text)
    show = showToSearch.replace("/searchS", "")
    if show != "":
        print('\n\n')
        print(">>Searching Show <<< "+show.upper()+" >>>")
        msg = update.message.reply_text("Searching Show...")
        showResult = api.searchShow(show)
        time.sleep(2)
        if len(showResult) != 0:
            msg.edit_text(str(len(showResult)) + ' Show(s) found')
            time.sleep(2)
            print(">>Show Found.. \n>> Generating Show Details..")
            for i in range(len(showResult)):
                 caption = api.generateShowCaption(showResult[i])
                 trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(showResult[i]))]])
                 #send feedback to user
                 context.bot.sendPhoto(chat_id = keys.groupId, photo = showResult[i]['poster'],caption = caption,parse_mode = ParseMode.HTML,reply_markup = trailer)
                 time.sleep(2)
            print("<< Show sent.")
            print('\n\n')
        else:
             msg.edit_text(R.notFound,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 



#get movie recommendations based on a given movie
def recommendMCommand(update,context):
    movieToFindRecommend = str(update.message.text)
    movieR = movieToFindRecommend.replace("/recommendM", "")
    if movieR != "":
        print('\n\n')
        print(">> Fetching Recommendations <<< "+movieR.upper()+" >>>")
        msg = update.message.reply_text("Finding Recommendations...")
        recommendedMovies = api.getRecommendedMovies(movieR)
        time.sleep(2)
        if len(recommendedMovies) != 0:
            print(">> Recommendations Found: "+str(len(recommendedMovies)))
            msg.edit_text(str(len(recommendedMovies)) + " Recommendation(s) Found")
            time.sleep(2)
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
             msg.edit_text(R.notFound,parse_mode=ParseMode.HTML)
    else:
         update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 

#get show recommendations based on a given show
def recommendSCommand(update,context):
    showToFindRecommend = str(update.message.text)
    showR = showToFindRecommend.replace('/recommendS',"")
    if showR != "":
        print('\n\n')
        print(">> Fetching Recommendations <<< "+showR.upper()+" >>>")
        msg = update.message.reply_text("Finding Recommendations...")
        recommendedShows = api.getRecommendedShows(showR)
        time.sleep(3)
        if len(recommendedShows) != 0:
            msg.edit_text(str(len(recommendedShows)) + " Recommendation(s) Found")
            time.sleep(2)
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
            msg.edit_text(R.notFound,parse_mode=ParseMode.HTML) 
    else:
         update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 



#discover movies
def discoverMCommand(update,context):
    print('\n\n')
    print(">> Discovering Movies")
    msg = update.message.reply_text("Discovering Movies...")
    dMovies = api.discoverMovies()
    time.sleep(3)
    print(">> Movies Discovered: "+ str(len(dMovies)))
    msg.edit_text(str(len(dMovies)) + " Movie(s) Discovered")
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
    msg = update.message.reply_text("Discovering Shows...")
    dShows = api.discoverShows()
    time.sleep(3)
    print(">> Discovered  Shows: "+ str(len(dShows)))
    msg.edit_text(str(len(dShows)) + " Show(s) Discovered")
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
    msg = update.message.reply_text("Fetching Trending Movies...")
    tMovies = api.trendingMovies()
    time.sleep(3)
    print(">> Trending Movies Found "+ str(len(tMovies)))
    msg.edit_text(str(len(tMovies)) + " Trending Movie(s) Found!")
    for i in range(len(tMovies)):
        caption = api.generateShowCaption(tMovies[i])
        trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(tMovies[i]))]])
        context.bot.sendPhoto(chat_id = keys.groupId, photo = tMovies[i]['poster'],caption = caption, reply_markup = trailer,parse_mode = ParseMode.HTML)
        print(">> Sending trending Movie: "+ str(i + 1))
        time.sleep(2)
    print("<< Total Movies Sent " + str(len(tMovies)))
    print('\n\n')

#get trending shows
def trendingSCommand(update,context):
    print('\n\n')
    print(">> Fetching Trending Shows")
    msg = update.message.reply_text("Fetching Trending Shows...")
    tShows = api.trendingShows()
    print(">> Trending Shows Found: "+ str(len(tShows)))
    msg.edit_text(str(len(tShows)) + ' Trending Show(s) Found')
    for i in range(len(tShows)):
        caption = api.generateShowCaption(tShows[i])
        trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(tShows[i]))]])
        context.bot.sendPhoto(chat_id = keys.groupId, photo = tShows[i]['poster'], caption = caption, reply_markup = trailer,parse_mode = ParseMode.HTML)
        print(">> Sending Trending Show: "+ str(i + 1))
        time.sleep(2)
    print("<< Total Shows Sent: " + str(len(tShows)))
    print('\n\n')

#search a torrent
def search1337x(update,context):
     search = str(update.message.text)
     item = search.replace('/searchT',"")
     if item != '':
         msg = update.message.reply_text("Searching..")
         time.sleep(2)
         URL_1337x = "https://www.1377x.to/sort-category-search/{}/Movies/seeders/desc/1"
         BASE_PAGE_URL = "https://www.1377x.to"
         #Get the search page
         scrap = r.get(URL_1337x.format(item))
         soup = BeautifulSoup(scrap.content,'html.parser')
         #Get all elements containing the particular item results
         results = soup.find_all("td",class_='coll-1 name')
         msg.edit_text(str(len(results)) + " Results Found!")
         time.sleep(2)
         #Get the link to each result item and store in a list
         movieLinks = []
         msg.edit_text("Working on Results...")
         for key,result in enumerate(results):
             #Get /torrent/file-name
             toResultLink = result.find_all('a')[1]['href']
             name = result.find_all('a')[1].string
             size = soup.find_all('td',class_="coll-4 size mob-uploader")[key].string
             seeder = soup.find_all('td',class_="coll-2 seeds")[key].string
             leechers =  soup.find_all('td',class_="coll-3 leeches")[key].string
             page = r.get(BASE_PAGE_URL + toResultLink)
             scrapp = BeautifulSoup(page.content, 'html.parser')
             #find the element with magnet link ans store in a variable
             Link = scrapp.find_all('ul')[3].li.a['href']
            #  time.sleep(2)
             magnetedMovie = {'name': name,'size': size,'link': Link,'seeds': seeder,'leeches': leechers}
             movieLinks.append(magnetedMovie)
             reply = R.link.format(name=name,size=size,link=Link,seed=seeder,leech=leechers)
             msg.reply_text(reply,parse_mode = ParseMode.HTML)
             time.sleep(2)
         return movieLinks
         


def requestCommand(update,context):
    requestedMovie = str(update.message.text) 
    movieStr = requestedMovie.replace("/request","",1)
    list =['movie','series']
    if movieStr != "":
        username = update.message.from_user['username']
        now = t.now()
        requestTime = now.strftime("%H:%M:%S, %d/%m/%y")
        request = '<b>Username: </b><i>'+str(username)+"</i>\n<b>Request: </b><i>"+str(movieStr)+ "</i>\n<b>Time: </b><i>"+ str(requestTime) + "</i>"
        context.bot.send_message(text=request,chat_id = keys.requestGroupId,parse_mode = ParseMode.HTML)
        time.sleep(5)
        print('\n\n')
        print(">> Requested movie : "+ movieStr.upper())
        # writeRequest(reqq=movieStr, uname=username)
        update.message.reply_text(R.requestSubmitted,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML)

def writeRequest(data):
    now = t.now()
    
    try:
        file = open(keys.file,'a') 
        file.write(data)
        file.write('\n\n')
        file.flush()
        file.close()
        # data = {'Username': uname,'Request': reqq,'Time': str(now)}
        # cloud.storeToCloud(data)
       
        print("<< Write successfull")
        print('\n\n')
    except IOError as error:
        print(error)

def handleMessage(update,context):
    text = str(update.message.text).lower()
    print("Here")
    name = update.message.from_user['username']
    response = R.sampleResponse(text).format(name)
    if response:
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

def error(update,context,error):
    print(f"Error {context.error}")
    
def weeklyTrending(context:CallbackContext):
        trendingMCommand()
        time.sleep(10)
        trendingSCommand()

# def sendMessages(message):
#     tries = 0
#     maxTries = 10
#     retry_delays = 10
#     while tries < maxTries:
#         try

def main():
    updater = Updater(keys.BOT_API_KEY, use_context=True,request_kwargs={'read_timeout':15,'connect_timeout': 15})
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
    j.run_daily(weeklyTrending,time= T.time(8,00), days= "4")

    #Handle torrent search
    dp.add_handler(CommandHandler('searchT',search1337x))


    dp.add_handler(CommandHandler('quote',quoteCommand))
    dp.add_handler(MessageHandler(Filters.text,handleMessage))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
