import requests
import json
from bs4 import BeautifulSoup
import api
import webbrowser

def get_image(id, mtype):
    # requires id, mtype (either album or artist)
    
    baseurl='https://open.spotify.com/{}/'.format(mtype)+ id
    print(baseurl)
    webbrowser.open_new(baseurl)
