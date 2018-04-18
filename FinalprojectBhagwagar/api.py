import secrets
import requests
import json
from pprint import pprint
from caching import *

client_key = secrets.client_key
client_secret = secrets.client_secret

grant_type='client_credentials'

body_params={'grant_type':grant_type}
authurl = 'https://accounts.spotify.com/api/token'
#auth = OAuth1(client_key, client_secret)
resp=requests.post(authurl, data=body_params, auth= (client_key, client_secret))
# resp=requests.post(url, headers={'Authorization' : 'Basic ' + client_key + ':' +client_secret},
# data={'grant_type':'client_credentials'})
json_resp=json.loads(resp.text)
token=json_resp['access_token']

def api_request(url=None, params={}):

    #Code for OAuth starts
    if url:
        baseurl=url
    else:
        baseurl= 'https://api.spotify.com/v1/search'


    data=make_request_using_cache(baseurl, headers={"Authorization": "Bearer " +token}, params=params)
    #data=requests.get(baseurl, headers={"Authorization": "Bearer " +token}, params=params)
    #print(data.url)
    return data

def get_artist_info(artist):
    params = {'type': 'artist', 'q': artist}
    data=api_request(params=params)
    infourl=(data['artists']['items'][0]['href'])
    artist_info=api_request(url=infourl)
    artistsname=artist_info['name']
    followercount=artist_info['followers']['total']
    popularitycount=artist_info['popularity']
    genres=artist_info['genres']
    artistid=artist_info['id']
    #pprint(genres)
    return [None, artistsname, followercount, popularitycount, str(genres), artistid]

def get_album_info(album):
    params = {'type': 'album', 'q': album}
    data=api_request(params=params)
    albumid=data['albums']['items'][0]['id']
    albumidurl='https://api.spotify.com/v1/albums/'+ albumid
    albumdata=api_request(url=albumidurl)
    albumname=albumdata['name']
    artistname=albumdata['artists'][0]['name']
    trackcount=(len(albumdata['tracks']['items']))
    release_date=(albumdata['release_date'])
    popularity=(albumdata['popularity'])
    albumid=albumdata['id']
    return [None, albumname, artistname, trackcount, release_date, popularity, albumid]
    # infourl=(data['artists']['items'][0]['href'])
    # artist_info=api_request(url=infourl)
    # print(artist_info)


get_artist_info('Chris Brown')
#get_musictest()

# term = input("enter artist name and album name: \n> ")
# get_artist_info(term)
