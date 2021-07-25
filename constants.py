#telegram bot api
API_KEY = '1751554864:AAFriVnMVRUjRk7EYeAbDVsNgMajSoJcyyI'
#moviedb search api link
movieSearchURL = "https://api.themoviedb.org/3/search/movie?api_key=f66022942583a57f9df36a479bd83639&query="
movieRecommendationURL = "https://api.themoviedb.org/3/movie/{}/recommendations?api_key=f66022942583a57f9df36a479bd83639&language=en-US"
#get poster image from moviesdb
baseImgLink = "https://image.tmdb.org/t/p/w500/"

groupId = -570113497
#Diplay content on different ocassions
kingsMovies = "\n\n😎<b> Endelea kufurahia burudani ya kishua kutoka King's Movies👑 🎥.</b>"
requestText = "\n\n<b>Tumia Command zifuatazo kupata huduma zetu:</b>\n\n"
requestText +=  '👉 <b>/request ["Jina La Movie/Series"]["Movie au Series?"]["Ya Mwaka Gani?"]</b> -> Request movie au series unayotaka\n\n'
requestText +=  '👉 <b>/report ["Mrejesho"]</b> -> Wasilisha mrejesho na changamoto kwa Admin\n\n'
requestText += '👉 <b>/search ["Jina la movie/series"] </b>-> Pata Taarifa fupi kuhusu movie husika\n\n'
requestText += '👉 <b>/quote </b>-> Neno la busara kupamba siku yako☀️\n\n'

quotesText = '☀️ Je, unahitaji kitu cha kupamba siku yako?\n'
quotesText += 'Andika /quote kupata maneno ya busara kupamba siku yako😊'

welcomeText = "Habari😃,\n<b> Karibu King's Movies👑 🎥 .</b>  \n\n"
welcomeText += "Mimi ni Dumbster, Msaidizi katika kupokea requests na kukuongoza katika Channel hii😊 "
welcomeText += requestText
welcomeText += ' \n\n<b>Andika /help muda wowote kupata maelekezo na msaada</b>'
welcomeText += kingsMovies
welcomeText += " \n \n \nAdmin : <b>@Nenghajm</b>"

help = "<b>Karibu😃 , Dumbster Bot here to help you!</b>"
help += requestText
help += kingsMovies

problemReported = "😃 Mrejesho umefikishwa kwa Admin. Tutashughulikia haraka iwezekanavyo.\n\n Asante kwa mchango wako wa thamani😊.\n"
problemReported += kingsMovies

emptyFeedback = "😢 Tafadhali kamilisha taarifa sahihi kwenye command ili tuweze kukuhudumia.\n\nAsante kwa mchango wako wa thamani😊"
emptyFeedback += kingsMovies

requestSubmitted = "😃 Request yako imewasilishwa."
requestSubmitted += "Tutatuma mrejesho punde tutakapo ipata!"
requestSubmitted += kingsMovies

kindNotStated = "😢 Tafadhali eleza kama request yako ni movie au series."
kindNotStated += "\n\nAndika /help kupata msaada zaidi."
kindNotStated += kingsMovies

textNotListed = "😢 Samahani, Mrejesho wako sio sahihi. "
textNotListed += "Tafadhali pitia muongozo kwa kuandika /start kisha jaribu tena"
textNotListed += kingsMovies





