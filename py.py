# TESTING PLAYGROUND NO ACTUAL FUNCTIONALITY

import requests as l
import datetime
import time
# DONE get searched movie https://api.themoviedb.org/3/search/movie?api_key=f66022942583a57f9df36a479bd83639&query=
#  DONE get recommendeded movie https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=f66022942583a57f9df36a479bd83639&language=en-US&page=1
# DONE discover movies https://api.themoviedb.org/3/discover/movie?api_key=f66022942583a57f9df36a479bd83639&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate
# DONE get trending movies & tv https://api.themoviedb.org/3/trending/all/day?api_key=f66022942583a57f9df36a479bd83639
# DONE get searched tv shows https://api.themoviedb.org/3/search/tv?api_key=f66022942583a57f9df36a479bd83639&query=
#  DONE get tv show recommendations https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key=f66022942583a57f9df36a479bd83639&language=en-US&page=1
# DONE discover tv shows https://api.themoviedb.org/3/discover/tv?api_key=f66022942583a57f9df36a479bd83639&language=en-US&sort_by=popularity.desc&page=1&timezone=America%2FNew_York&include_null_first_air_dates=false&watch_region=us&with_watch_monetization_types=flatrate
# discover movies by company
#discover movies by casts
# interactivity when performing background processes
# setting up passwords to gain bot access

# dots=["."*8]
# print(dots)
# i = 5
# for i < 5:
#    for i in dots:
#        print(i,end="")
#        sleep(.5)

from time import sleep
greetings = ['hey','hello','mambo','hi','hellow']
test = "hey"
if  test in greetings:
    print(test)



#Clickable link to download torrents
#Optimize other area in searching shows and movies(Modify get****Details functions)
#Intense Testing
#Interactive Keyboard during requests