Welcome to my project!

In my SI 206 Final Project, I have used Spotify to obtain information about popular artists and albums.
 
Essentially, my program takes in inputs (an album name or an artist name) and gives more information about this including popularity, artists name, followers, genres, etc using interactive capabilities. The user has the option to go even further with this informationa and see visuals including a photo of the album/artist along with graphs to compare the chosen album/artist to Beyonce in terms of popularity and following account (because Beyonce is a standard to compare :) ).

In order to do this, I used the Spotify API and Webscraping. To get the Spotify API you will need to go to ( https://developer.spotify.com/web-api/). You will need to generate your own API Client key and Client secret and input them in a secrets.py file. You can find the plotly information in this link (https://plot.ly/python/bar-charts/)

Because this is fetching live data (since big artists such as Beyonce and Big Sean have following counts that change by the second), you will need to run the testing.py function. This allows you to test the code as well as run it. 

This code contains 5 significant parts: the interactive means, the database collection (to return history of the user), webscraping, api/oauth, and plotly. There are files to represent each part and differentiate it (classes are used in the testing functions).

Running the testing.py function-- or if you do not want to test the code and trust the code, you can run the interactive.py function-- will take the user to the main menu prompt. They can either select an album name or an artist name and get detailed information (get_album_info(album)/get_artist_info(artist)) in the api.py about it as well as see their previous search history which is stored in the DataBase. After seeing this information, they can go further to see graphs or images and return back to the main menu. 

I hope you enjoy the program :)
