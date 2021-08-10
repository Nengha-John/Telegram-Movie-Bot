#Diplay content on different ocassions
ngMovies = "\n\n<b>NG Movies,\nYour Entertainment Partner!😎.\n<b>Help Us Grow😊 : 0684274128</b>\nAdmin: @dumbster1 </b>"
requestText = "\n\n<b>Use the following commands to Explore Our Entertainment:</b>\n\n"
requestText += '👉  <b>/request <i>Movie Name</i></b> -->  Request a Movie or Series\n\n'
requestText += '👉  <b>/searchm <i>Movie Name</i></b> -->  Search Movie Description and Trailer\n\n'
requestText += '👉  <b>/searchs <i>TV Series Name</i> </b>-->  Search TV Series Description and Trailer\n\n'
requestText += '👉  <b>/searcht <i>Movie Name</i> </b>-->  Search Movie Torrent on 1337x\n\n'
requestText += '👉  <b>/recommendm <i>Movie Name</i> </b>-->  Get Movie Recommendations based on Movie Name\n\n'
requestText += '👉  <b>/recommends <i>TV Series Name</i> </b>-->  Get TV Shows Recommendations based on Series Name\n\n'
requestText += '👉  <b>/discoverm </b>-->  Discover Random Movies \n\n'
requestText += '👉  <b>/discovers </b>-->  Discover TV Series\n\n'
requestText += '👉  <b>/upcomingm </b>-->  Get Upcoming Movies\n\n'
requestText += '👉  <b>/quote </b>-> Get a Random Quote to Lighten your Day☀️\n\n'
requestText += '👉  <b>/help </b>-> Get help \n\n'
requestText += '👉  <b>Our Channel sends Weekly Trending Movies and Series every Friday 08:00. Stay Tuned😎.</b>'


welcomeText = "<b> Welcome to NG Movies 👑 🎥 .</b>  \n\n"
welcomeText += "Your favourite Telegram Channel to get Movie Updates😎. Request your favourite movies and have them delivered in your inbox. "
welcomeText += "Only at NG Movies!!"
welcomeText += requestText
welcomeText += ngMovies


help = "<b>DumbsterBot here to help you!</b>"
help += "\n\n<b> For any inconviniences, report to Admin @dumbster1</b>\n"
help += requestText
help += ngMovies


emptyFeedback = "😢 Please provide a Movie or Series name."
emptyFeedback += ngMovies

requestSubmitted = "😃 Your request has been submitted. "
requestSubmitted += "We will process Your Request as soon as possible. Stay tuned😎!"
requestSubmitted += ngMovies

#Not found errors
notFound = "Found 0 results😢 . Check your entry and try again"
greeting = "\n Welcome to NG Movies 👑 🎥. \nType /start to get started.\n\n "
offensive = " Offensive language is not allowed in our group. It could lead to permanent barn from group"
#1337x scrapper reply text skeleton
link = "<b>Name:</b>  <i>{name}</i>\n<b>Size:</b> <i>{size}</i>\n<b>Seeders:</b> <i>{seed}</i>\n<b>Leechers:</b> <i>{leech}</i>\n <b>Magnet Link:\n\n</b>{link}"
testing = "DumbsterBot Testing 1 2 3...."

def sampleResponse(text):
    greetings = ['hey','hello','mambo','hi','hellow']
    matusi = ['msenge','kuma','usenge','msng','kmk']
    response = " "
    if text in greetings:
       response = "Hello, <b>{}</b>😊. "+ greeting
    if text in matusi:
       response = "Sorry <b>{}</b>😢. " + offensive
    return response


