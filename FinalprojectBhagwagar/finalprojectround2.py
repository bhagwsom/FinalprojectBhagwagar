import json
from bs4 import BeautifulSoup
import requests
import secrets
from requests_oauthlib import OAuth1
import sqlite3
import csv
DBNAME = 'Spotify.db'

CACHE_FNAME='cache_file_name.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def make_request_using_cache(search_term):
    unique_ident = search_term
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        resp = get_music()
        CACHE_DICTION[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]




def get_music():
    client_key = secrets.client_key
    client_secret = secrets.client_secret

    grant_type='client_credentials'

    body_params={'grant_type':grant_type}
    #Code for OAuth starts
    url = 'https://accounts.spotify.com/api/token'
    #auth = OAuth1(client_key, client_secret)
    resp=requests.post(url, data=body_params, auth= (client_key, client_secret), params={"type":"album"})
    # resp=requests.post(url, headers={'Authorization' : 'Basic ' + client_key + ':' +client_secret},
    # data={'grant_type':'client_credentials'})
    json_resp=json.loads(resp.text)
    token=json_resp['access_token']
    data=requests.get("https://api.spotify.com/v1/albums/0sNOF9WDwhWunNAHPD3Baj", headers={"Authorization": "Bearer " +token})#requests.get('https://api.spotify.com/v1/albums/0sNOF9WDwhWunNAHPD3Baj', headers={'authorization': 'Bearer' + token})
    return data

def init_db_json():
    conn =sqlite3.connect(DBNAME)
    cur=conn.cursor()

    statement='''
        DROP TABLE IF EXISTS 'Albums';
        '''
    cur.execute(statement)
    statement='''
        CREATE TABLE 'Albums'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'AlbumName' TEXT NOT NULL,
            'ArtistName' TEXT NOT NULL,
            'ReleaseDate' TEXT NOT NULL,
            'TrackCount' TEXT NOT NULL

        );
    '''
    cur.execute(statement)

    statement='''
        DROP TABLE IF EXISTS 'Artists';
        '''
    cur.execute(statement)
    statement='''
        CREATE TABLE 'Artists'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'ArtistName' TEXT NOT NULL
        );
    '''
    cur.execute(statement)

    statement='''
        DROP TABLE IF EXISTS 'Tracks';
        '''
    cur.execute(statement)
    statement='''
        CREATE TABLE 'Tracks'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'ArtistName' TEXT NOT NULL,
            'AlbumName' TEXT NOT NULL,
            'TrackLength' INTEGER NOT NULL
        );
            '''
    cur.execute(statement)

    conn.commit()
    conn.close()
#inserting the data
def insert_data():
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    for x in CACHE_FNAME:
        insertion=(None, x['data']['artists'][0]['name'])
        statment= 'INSERT INTO "Artists"'
        statement += 'VALUES(?,?)'
        cur.execute(statement, insertion)
    conn.commit()


    for x in CACHE_FNAME:
        insertion=(None, x['data']['artists'][0]['name'], x['data']['name'], x['data'], x['data']['tracks']['items'][0]['duration_ms'])
        statement= 'INSERT INTO "Tracks"'
        statement += 'VALUES(?, ?, ?, ?)'
        cur.execute(statement, insertion)
    conn.commit()
'''

    for x in CACHE_FNAME:
        if x['type'] == 'track':
            insertion= (None, x['data']['name'], x['data']['artist'][0], x['data']['release_date'], )
            for t in x['tracks']['items']:
                insertion +=


make_request_using_cache('data')
'''
