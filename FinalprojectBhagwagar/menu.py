main_menu='''
    Welcome! What would you like to do? (Enter the number followed by the search term)
    1. Search Artists (input: {artist's name})
    2. Search Albums (input: {artist's name} {album's name})
    3. View Your History
    4. Quit
    '''

album_menu='''
    Album Name: {}
    Artist Name: {}
    Track Count: {}
    Release Date: {}
    Popularity: {}
    Do you want to see more details?
    '''
detailed_album_menu='''
    1. Graph 1: Compare Track Count to Beyonce
    2. Graph 2: Compare Popularity to Beyonce
    3. Image
    4. No, I changed my mind
    '''

artist_menu='''
    Artist Name: {}
    Follower Count: {}
    Popularity Count: {}
    Genres: {}
    Do you want to see more details?
    '''

detailed_artist_menu= '''
    1. Graph 1: Compare Follower Count to Beyonce
    2. Graph 2: Compare Popularity to Beyonce
    3. Image
    4. No, I changed my mind
    '''

def refresh():
    print('\n'*25)


def pressenter():
    input('press enter to continue')
