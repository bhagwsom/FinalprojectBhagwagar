import json
from bs4 import BeautifulSoup
import requests
import secrets
from requests_oauthlib import OAuth1


DBNAME = 'Spotify.db'

CACHE_FNAME='cache_file_name.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def params_unique_combination(baseurl, params):
    alphabetized_keys = sorted(params.keys())
    res = []
    for k in alphabetized_keys:
        k.replace(" ","+")
        res.append("{}={}".format(k, params[k]))
    return baseurl + "?" + "&".join(res)


def make_request_using_cache(baseurl, headers, params):
    unique_ident = params_unique_combination(baseurl, params)
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(baseurl, headers = headers, params=params)
        CACHE_DICTION[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]
