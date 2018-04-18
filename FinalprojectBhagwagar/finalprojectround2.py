import json
from bs4 import BeautifulSoup
import requests
import secrets
from requests_oauthlib import OAuth1
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
