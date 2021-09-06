import constants as keys
import moviesApi as api
from telegram.ext import *
import telegram
import responses as R
import requests as r
from telegram import ParseMode
from datetime import datetime as t
from datetime import timedelt
import datetime as T
import time
from bs4 import BeautifulSoup 
print("Bot Started")


def startCommand(update,context):
    update.message.reply_text(R.welcomeText,parse_mode=ParseMode.HTML)


def helpCommand(update,context):
    update.message.reply_text(R.help,parse_mode=ParseMode.HTML)

def checkAdmin(update, context):
    admins = ['creator','administrator']
    user = context.bot.getChatMember(user_id=update.message.from_user.id,chat_id=update.message.chat.id)
    if user['status'] in admins:
        return True
    else:
        return False

#search movie command
def searchMCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
        print('is Admin')
        movieToSearch = str(update.message.text)
        movie = movieToSearch.replace("/searchm", "")
        movie = movie.replace('@dumbsterBot','')
       
        if movie:
            print('\n\n')
            print(">>Searching Movie <<" + movie.upper() +" >>")

            msg = update.message.reply_text("Searching Movie...")
            movieResult = api.searchMovie(movie)
            try:
                movieResult = api.searchMovie(movie)
            except error:
                print(error)
                msg.edit_text(error)

            if len(movieResult) != 0:
                msg.edit_text( "Movie Found!!")
                print('>>Movie Found..\n>>Generating Movie Details..')
                time.sleep(2)

    #              for i in range(len(movieResult)):
                caption = api.generateMovieCaption(movieResult[0])
                trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(movieResult[0]))]])
    #              print("Movie " + str(i+1) + " of " + str(len(movieResult)) + ' sent.')
                #send feedback to user
                context.bot.sendPhoto(chat_id = keys.groupId, photo = movieResult[0]['poster'],caption = caption,parse_mode = ParseMode.HTML,reply_markup = trailer)
                time.sleep(2)

                print("<< Movie Sent.")
                print('\n\n')
            else:
                print(">>Movie not Found")
                msg.edit_text(R.notFound,parse_mode=ParseMode.HTML) 
        else:
            update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)


#search show command
def searchSCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            showToSearch = str(update.message.text)
            show = showToSearch.replace("/searchs", "")
            show = show.replace('@dumbsterBot','')

            if show != "":
                print('\n\n')
                print(">>Searching Show <<< "+show.upper()+" >>>")

                msg = update.message.reply_text("Searching Show...")
                try:
                    showResult = api.searchShow(show)
                except:
                    msg.edit_text(error)

                if len(showResult) != 0:
                    msg.edit_text('Show found')
                    time.sleep(2)

        #             print(">>Show Found.. \n>> Generating Show Details..")
        #             for i in range(len(showResult)):
                    caption = api.generateShowCaption(showResult[0])
                    trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(showResult[0]))]])
                    #send feedback to user
                    context.bot.sendPhoto(chat_id = keys.channelID, photo = showResult[0]['poster'],caption = caption,parse_mode = ParseMode.HTML,reply_markup = trailer)
        #             print("Movie " + str(i+1) + " of " + str(len(showResult)) + ' sent.')
                    time.sleep(2)

                    print("<< Show sent.")
                    print('\n\n')
                else:
                    msg.edit_text(R.notFound,parse_mode=ParseMode.HTML)
            else:
                update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)



#get movie recommendations based on a given movie
def recommendMCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            movieToFindRecommend = str(update.message.text)
            movieR = movieToFindRecommend.replace("/recommendm", "")
            movieR = movieR.replace('@dumbsterBot','')

            if movieR != "":
                print('\n\n')
                print(">> Fetching Recommendations <<< "+movieR.upper()+" >>>")

                msg = update.message.reply_text("Finding Recommendations...")
                try:
                    recommendedMovies = api.getRecommendedMovies(movieR)
                except error:
                    msg.edit_text(error)


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
                        time.sleep(3)

                    print('<< Total Recommendations Sent: ' + str(len(recommendedMovies)))
                    print('\n\n')

                else:
                    msg.edit_text(R.notFound,parse_mode=ParseMode.HTML)

            else:
                update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)

#get show recommendations based on a given show
def recommendSCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            showToFindRecommend = str(update.message.text)
            showR = showToFindRecommend.replace('/recommends',"")
            showR = showR.replace('@dumbsterBot','')

            if showR != "":
                print('\n\n')
                print(">> Fetching Recommendations <<< "+showR.upper()+" >>>")
                msg = update.message.reply_text("Finding Recommendations...")
                try:
                    recommendedShows = api.getRecommendedShows(showR)
                except:
                    msg.edit_text(error)

                if len(recommendedShows) != 0:
                    msg.edit_text(str(len(recommendedShows)) + " Recommendation(s) Found")
                    time.sleep(2)

                    print(">> Recommendations Found: "+ str(len(recommendedShows)))
                    print(">>Working on Recommendations...")

                    for i in range(len(recommendedShows)):
                        caption = api.generateShowCaption(recommendedShows[i])
                        trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(recommendedShows[i]))]])
                        context.bot.sendPhoto(chat_id = keys.channelID, photo = recommendedShows[i]['poster'],caption = caption, reply_markup = trailer, parse_mode = ParseMode.HTML)
                        print(">> Sending Recommendation "+ str(i + 1))
                        time.sleep(3)

                    print('<< Total Recommendations sent: ' + str(len(recommendedShows)))
                    print('\n\n')
                else:
                    msg.edit_text(R.notFound,parse_mode=ParseMode.HTML) 

            else:
                update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML) 
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)


#discover movies
def discoverMCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            print('\n\n')
            print(">> Discovering Movies")

            msg = update.message.reply_text("Discovering Movies...")
            try:
                dMovies = api.discoverMovies()
            except:
                msg.edit_text(error)
            

            print(">> Movies Discovered: "+ str(len(dMovies)))
            msg.edit_text(str(len(dMovies)) + " Movie(s) Discovered")

            for i in range(len(dMovies)):
                caption = api.generateMovieCaption(dMovies[i])
                trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(dMovies[i]))]])
                context.bot.sendPhoto(chat_id = keys.requestGroupId, photo = dMovies[i]['poster'],caption = caption, reply_markup = trailer, parse_mode = ParseMode.HTML)
                print(">> Sending Discovered Movie: "+ str(i + 1))
                time.sleep(2)

            print("<< Total Movies Sent " + str(len(dMovies)))
            print('\n\n')
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)


#discover shows
def discoverSCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            print('\n\n')
            print(">> Discovering Shows")

            msg = update.message.reply_text("Discovering Shows...")
            try:
                dShows = api.discoverShows()
            except:
                msg.edit_text(error)


            print(">> Discovered  Shows: "+ str(len(dShows)))
            msg.edit_text(str(len(dShows)) + " Show(s) Discovered")

            for i in range(len(dShows)):
                caption = api.generateShowCaption(dShows[i])
                trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(dShows[i]))]])
                context.bot.sendPhoto(chat_id = keys.requestGroupId, photo = dShows[i]['poster'],caption = caption, reply_markup = trailer, parse_mode = ParseMode.HTML)
                print(">> Sending Discovered Movie: "+ str(i + 1))
                time.sleep(2)

            print("<< Total Shows Sent: " + str(len(dShows)))
            print('\n\n')
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)



#get trending movies
def trendingMCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            print('\n\n')
            print(">> Fetching Trending Movies")

            msg = update.message.reply_text("Fetching Trending Movies...")
            tMovies = api.trendingMovies()
            time.sleep(2)

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
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)



#get trending shows
def trendingSCommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            print('\n\n')
            print(">> Fetching Trending Shows")
            
            msg = update.message.reply_text("Fetching Trending Shows...")
            try:
              tShows = api.trendingShows()
            except:
                msg.edit_text(error)
            print(">> Trending Shows Found: "+ str(len(tShows)))
            msg.edit_text(str(len(tShows)) + ' Trending Show(s) Found')

            for i in range(len(tShows)):
                caption = api.generateShowCaption(tShows[i])
                trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(tShows[i]))]])
                context.bot.sendPhoto(chat_id = keys.channelID, photo = tShows[i]['poster'], caption = caption, reply_markup = trailer,parse_mode = ParseMode.HTML)
                print(">> Sending Trending Show: "+ str(i + 1))
                time.sleep(2)

            print("<< Total Shows Sent: " + str(len(tShows)))
            print('\n\n')
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)

#get upcoming movies
def upcomingMcommand(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
        print('\n\n')
        print(">> Fetching Upcoming Movies")

        msg = update.message.reply_text("Fetching Upcoming Movies...")
        uMovies = api.upcomingMovies()
        time.sleep(2)

        print(">> Upcoming Movies Found "+ str(len(uMovies)))
        msg.edit_text(str(len(uMovies)) + " Upcoming Movie(s) Found!")

        for i in range(len(uMovies)):
            caption = api.generateShowCaption(uMovies[i])
            trailer = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton('Trailer',url = api.getTrailerLink(uMovies[i]))]])
            context.bot.sendPhoto(chat_id = keys.groupId, photo = uMovies[i]['poster'],caption = caption, reply_markup = trailer,parse_mode = ParseMode.HTML)
            print(">> Sending Upcoming Movie: "+ str(i + 1))
            time.sleep(2)

        print("<< Total Movies Sent " + str(len(uMovies)))
        print('\n\n')
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)

#search a movie torrent
def search1337xMovie(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            search = str(update.message.text)
            item = search.replace('/searcht',"")
            item = item.replace('@dumbsterBot','')

            if item != '':
                msg = update.message.reply_text("Searching..")
                time.sleep(2)
                print('Scrapping 1337x...')
                URL_1337x = "https://www.1377x.to/sort-category-search/{}/Movies/seeders/desc/1"
                BASE_PAGE_URL = "https://www.1377x.to"

                #Get the search page
                scrap = r.get(URL_1337x.format(item))
                soup = BeautifulSoup(scrap.content,'html.parser')
                #Get all elements containing the particular item results
                results = soup.find_all("td",class_='coll-1 name')
                msg.edit_text(str(len(results)) + " Results Found!")
                print("Found " + str(len(results)))
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
                    magnetedMovie = {'name': name,'size': size,'link': Link,'seeds': seeder,'leeches': leechers}
                    movieLinks.append(magnetedMovie)
                    reply = R.link.format(name=name,size=size,link=Link,seed=seeder,leech=leechers)
                    msg.reply_text(reply,parse_mode = ParseMode.HTML)
                    print("Torrent " + str(key+1) + " of " + str(len(results)) + ' sent.')
                    time.sleep(2)
            else:
                update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML)
            return movieLinks
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)     


#search a TV torrent
def search1337xTV(update,context):
    isAdmin = checkAdmin(update=update,context=context)
    uName = update.message.from_user['first_name']
    if isAdmin:
            search = str(update.message.text)
            item = search.replace('/searcht',"")
            item = item.replace('@dumbsterBot','')

            if item != '':
                msg = update.message.reply_text("Searching..")
                time.sleep(2)
                print('Scrapping 1337x...')
                URL_1337x = "https://www.1377x.to/sort-category-search/{}/TV/seeders/desc/1"
                BASE_PAGE_URL = "https://www.1377x.to"

                #Get the search page
                scrap = r.get(URL_1337x.format(item))
                soup = BeautifulSoup(scrap.content,'html.parser')
                #Get all elements containing the particular item results
                results = soup.find_all("td",class_='coll-1 name')
                msg.edit_text(str(len(results)) + " Results Found!")
                print("Found " + str(len(results)))
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
                    magnetedMovie = {'name': name,'size': size,'link': Link,'seeds': seeder,'leeches': leechers}
                    movieLinks.append(magnetedMovie)
                    reply = R.link.format(name=name,size=size,link=Link,seed=seeder,leech=leechers)
                    msg.reply_text(reply,parse_mode = ParseMode.HTML)
                    print("Torrent " + str(key+1) + " of " + str(len(results)) + ' sent.')
                    time.sleep(2)
            else:
                update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML)
            return movieLinks
    else:
        update.message.reply_text(R.notAdmin.format(name=uName),parse_mode=ParseMode.HTML)     


def requestCommand(update,context):
    requestedMovie = str(update.message.text) 
    movieStr = requestedMovie.replace("/request","",1)
    movieStr = movieStr.replace('@dumbsterBot','')
    list =['movie','series']

    if movieStr != "":
        username = update.message.from_user['first_name']
        now = t.now() + timedelta(hours=3)
        requestTime = now.strftime("%H:%M:%S, %d/%m/%y")

        request = '<b>Username: </b><i>'+str(username)+"</i>\n<b>Request: </b><i>"+str(movieStr)+ "</i>\n<b>Time: </b><i>"+ str(requestTime) + "</i>"
        context.bot.send_message(text=request,chat_id = keys.requestGroupId,parse_mode = ParseMode.HTML)
        time.sleep(5)

        print('\n\n')
        print(">> "+ username + "Requested movie : "+ movieStr.upper())

        # writeRequest(reqq=movieStr, uname=username)
        update.message.reply_text(R.requestSubmitted,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(R.emptyFeedback,parse_mode=ParseMode.HTML)



def handleMessage(update,context):
    text = str(update.message.text).lower()
    name = update.message.from_user['username']
    response = R.sampleResponse(text).format(name)
    if response != " ":
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



def main():
    
    updater = Updater(keys.BOT_API_KEY, use_context=True,request_kwargs={'read_timeout':30,'connect_timeout': 30})
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', startCommand))
    dp.add_handler(CommandHandler('help', helpCommand))
    dp.add_handler(CommandHandler("request", requestCommand))

    # Handle search commands
    dp.add_handler(CommandHandler('searchm', searchMCommand))
    dp.add_handler(CommandHandler('searchs', searchSCommand))

    #Handle recommendations
    dp.add_handler(CommandHandler('recommendm', recommendMCommand))
    dp.add_handler(CommandHandler('recommends', recommendSCommand))
    
    #Handle discover commands
    dp.add_handler(CommandHandler('discoverm', discoverMCommand))
    dp.add_handler(CommandHandler('discovers', discoverSCommand))

    #Handle trending commands
    dp.add_handler(CommandHandler('trendingm',trendingMCommand))
    dp.add_handler(CommandHandler('trendings', trendingSCommand))
    
    #Handle upcoming commands
    dp.add_handler(CommandHandler('upcomingm',upcomingMcommand))


    #Testing scheduled messaging
    j = updater.job_queue
    j.run_daily(weeklyTrending,time= T.time(8,00), days= "4")

    #Handle  movie torrent search
    dp.add_handler(CommandHandler('searchtm',search1337xMovie))

    #Handle  TV torrent search
    dp.add_handler(CommandHandler('searchts',search1337xTV))


    dp.add_handler(CommandHandler('quote',quoteCommand))
    dp.add_handler(MessageHandler(Filters.text,handleMessage))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
