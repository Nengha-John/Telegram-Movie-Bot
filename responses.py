#Diplay content on different ocassions
kingsMovies = "\n\n<b>King's Movies,\nYour Entertainment Partner!😎.\n<b>Help Us Grow😊 : 0684274128</b>\nAdmin: @dumbster1 </b>"
requestText = "\n\n<b>Use the following commands to Explore Our Entertainment:</b>\n\n"
requestText += '👉  <b>/request <i>Movie Name</i></b> -->  Request a Movie or Series of your Choice and have it delivered to you\n'
requestText += '👉  <b>/searchM <i>Movie Name</i></b> -->  Search Movie Description and Trailers\n'
requestText += '👉  <b>/searchS <i>TV Series Name</i> </b>-->  Search TV Series Description and Trailers\n'
requestText += '👉  <b>/searchT <i>Movie Name</i> </b>-->  Search Movie Torrent on 1337x website\n'
requestText += '👉  <b>/recommendM <i>Movie Name</i> </b>-->  Get Movie Recommendations based on Movie Name\n'
requestText += '👉  <b>/recommendS <i>TV Series Name</i> </b>-->  Get TV Shows Recommendations based on Movie Name\n'
requestText += '👉  <b>/discoverM </b>-->  Discover Random Movies from different times and genres\n'
requestText += '👉  <b>/discoverS </b>-->  Discover TV Series Movies from different Times and Genres\n'
requestText += '👉  <b>/quote </b>-> Get a Random Quote to Lighten your Day☀️\n'
requestText += '👉  <b>/help </b>-> Get help \n\n'
requestText += '👉  <b>Our Channel sends Weekly Trending Movies and Series every Friday 08:00. Stay Tuned😎.</b>'


welcomeText = "<b> Welcome to King's Movies👑 🎥 .</b>  \n\n"
welcomeText += "Your favourite Telegram Channel to get Movie Updates😎. Request your favourite movies and have them delivered in your inbox. "
welcomeText += "Only at King's Movies!!"
welcomeText += requestText
welcomeText += kingsMovies


help = "<b>DumbsterBot here to help you!</b>"
help += "\n\n<b> For any inconviniences, report to Admin @dumbster1</b>\n"
help += requestText
help += kingsMovies


emptyFeedback = "😢 Please fill out the entry to use our Services."
emptyFeedback += kingsMovies

requestSubmitted = "😃 Your request has been submitted. "
requestSubmitted += "We will process Your Request as soon as possible. Stay tuned😎!"
requestSubmitted += kingsMovies

#Not found errors
notFound = "Found 0 results😢 . Check your entry and try again"
greeting = "\n Welcome to Kings Movies 👑 🎥. \nType /start to get started.\n\n "
offensive = " Offensive language is not allowed in our group. It could lead to permanent barn from group"
#1337x scrapper reply text skeleton
link = "<b>Name:</b>  <i>{name}</i>\n<b>Size:</b> <i>{size}</i>\n<b>Seeders:</b> <i>{seed}</i>\n<b>Leechers:</b> <i>{leech}</i>\n <b>Magnet Link:\n\n</b> <a href={link}>Click here to Download this Torrent</a>"
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


