#Diplay content on different ocassions
ngMovies = "\n\n<b>NG Movies,\nYour Entertainment Partner!😎.\n\nAdmin: @dumbster1 </b>"
requestText = "\n\n<b>Dumbster helps to collect request and a little fun with the following commands:</b>\n\n"
requestText += '👉  <b>/request <i>Movie Name</i></b> -->  Request a Movie or Series\n\n'
# requestText += '👉  <b>/searchm <i>Movie Name</i></b> -->  Search Movie Description and Trailer\n\n'
# requestText += '👉  <b>/searchs <i>TV Series Name</i> </b>-->  Search TV Series Description and Trailer\n\n'
# requestText += '👉  <b>/searcht <i>Movie Name</i> </b>-->  Search Movie Torrent on 1337x\n\n'
# requestText += '👉  <b>/recommendm <i>Movie Name</i> </b>-->  Get Movie Recommendations based on Movie Name\n\n'
# requestText += '👉  <b>/recommends <i>TV Series Name</i> </b>-->  Get TV Shows Recommendations based on Series Name\n\n'
# requestText += '👉  <b>/discoverm </b>-->  Discover Random Movies \n\n'
# requestText += '👉  <b>/discovers </b>-->  Discover TV Series\n\n'
# requestText += '👉  <b>/upcomingm </b>-->  Get Upcoming Movies\n\n'
requestText += '👉  <b>/quote </b>-> Get a Random Quote to Lighten your Day☀️\n\n'
requestText += '👉  <b>/help </b>-> Get help \n\n'
requestText += '<b>Dumbster sends Weekly Trending and Upcoming Movies and Series. Stay Tuned😎.</b>\n\n'
requestText += '<b>For any problems report to Admin: @dumbster1</b>'

welcomeText = "<b> Welcome to NG Movies 👑 🎥 .</b>  \n\n"
welcomeText += "<b>Your favourite Telegram Channel to get Movie Updates😎. Request your favourite movies and have them delivered.</b> "
welcomeText += "<b>Our Groups are managed by our favourite bot (Dumbster🤓).</b>"
welcomeText += requestText
welcomeText += ngMovies


help = "<b>Dumbster🤓 here to help you!</b>"
help += requestText
help += ngMovies


emptyFeedback = "😢 Please provide a Movie or Series name."
emptyFeedback += "\n\n Example:   /request Fast and Furious 9"
emptyFeedback += ngMovies

requestSubmitted = "😃 Your request has been submitted. "
requestSubmitted += "We will process Your Request as soon as possible. Stay tuned😎!"


#Not found errors
notFound = "Found 0 results😢 . Check your entry and try again"
greeting = "\n Welcome to NG Movies 👑 🎥. \nType /start to get started.\n\n "
offensive = " Offensive language is not allowed in our group. It could lead to permanent barn from group"
#1337x scrapper reply text skeleton
link = "<b>Name:</b>  <i>{name}</i>\n<b>Size:</b> <i>{size}</i>\n<b>Seeders:</b> <i>{seed}</i>\n<b>Leechers:</b> <i>{leech}</i>\n <b>Magnet Link:\n\n</b>{link}"
testing = "DumbsterBot Testing 1 2 3...."


#Other Errors
notAdmin = "Sorry, {name}. This command is for Admins only. Use /help to see possible commands. \n\n For any problems report to admin: @dumbster1"
adminTxt = 'Sorry our Admin is currently not available, Make your request and I will have it delivered. Type /start to get started.'

def sampleResponse(text):
    greetings = ['hey','hello','mambo','hi','hellow']
    matusi = ['msenge','kuma','usenge','msng','kmk','fala','boya','kumamake']
    admin = ['german','german machine','nenga','nengha','amon','amone']
    response = " "
    if text in greetings:
       response = "Hello, <b>{}</b>😊. "+ greeting
    if text in matusi:
       response = "Sorry <b>{}</b>😢. " + offensive
    if text in admin:
       response = "Hello, <b>{}</b>😊. " + adminTxt
    return response


