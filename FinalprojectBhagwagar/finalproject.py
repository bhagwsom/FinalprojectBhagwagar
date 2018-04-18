import json
from bs4 import BeautifulSoup
import requests
import secrets
from requests_oauthlib import OAuth1
import sqlite3
import csv

try:
    fref=open('cache_data.json', 'r')
    data=fref.read()
    CACHE_DICT= json.loads(data)
    fref.close()
except:
    CACHE_DICT={}

def get_data_using_cache(baseurl):
    #logging in
    #This URL will be the URL that your login form points to with the "action" tag.
    POST_LOGIN_URL = 'https://www.instagram.com/accounts/login/'

    unique_ident=baseurl
    #username-input-name is the "name" tag associated with the username input field of the login form.
    #password-input-name is the "name" tag associated with the password input field of the login form.
    payload = {
        'username': secrets.username,
        'password': secrets.password
    }

    if baseurl in CACHE_DICT:
        return CACHE_DICT[unique_ident]
    else:
        s = requests.session()
        s.post(POST_LOGIN_URL, data=payload)
        r = s.get(baseurl)
        #print(r.text)

        CACHE_DICT[unique_ident]=r.text
        fref=open('cache_data.json', 'w')
        dumped_data=json.dumps(CACHE_DICT, indent=2)
        fref.write(dumped_data)
        fref.close()
        return CACHE_DICT[baseurl]

#part 2 Caching
try:
    fref2=open('cache_data2.json', 'r')
    data2=fref2.read()
    CACHE_DICT2= json.loads(data2)
    fref2.close()
except:
    CACHE_DICT2={}

def get_following_info():
    #This URL is the page you actually want to pull down with requests.
    baseurl = 'https://www.instagram.com/studentsofumich/followers'

    page_html=get_data_using_cache(baseurl)
    page_soup=BeautifulSoup(page_html, 'html.parser')

    #Getting following list
    data=page_soup.find_all(class_="_p4iax") #class_="_t98z6 _sf8d3" href="/studentsofumich/following/"

    accounts_following=[]
    for following in data:
            accounts_following=following.find_all(class_='_2g7d5 notranslate _o5iw8')

    print(data)
    #To get info about the accounts
#     for x in accounts_following:
#         if x.text == state_abbr_dict[state_abbr]:
#             site_info=x.find('a')['href']
#
#     stateurl= baseurl+ site_info
#     site_data=get_data_using_cache(stateurl)
#     page_soup=BeautifulSoup(site_data, 'html.parser')
#
#     #getting the content for each state link
#     site_content=page_soup.find(class_="col-md-9 col-sm-12 col-xs-12 stateCol")
#     site_list= site_content.find_all(class_="clearfix")
#     #print(site_content)
#     for x in site_list:
#         park_name=x.find('h3').text
#         park_type=x.find('h2').text
#         park_description= x.find('p').text
#         #To get the physical address
#         closerlook=x.find('a')['href']
#         closerlookurl=baseurl + closerlook
#         closer=get_data_using_cache(closerlookurl)
#         closer_soup=BeautifulSoup(closer, 'html.parser')
#         park_address=closer_soup.find(class_="mailing-address")
#         try:
#             address= park_address.find(itemprop="streetAddress").text.strip()
#         except:
#             address= park_address.find(class_='adr').text.strip() + ' '+park_address.find(itemprop='postOfficeBoxNumber').text.strip()
#         city= park_address.find(itemprop="addressLocality").text
#         state=park_address.find(itemprop="addressRegion").text
#         zipcode=park_address.find(itemprop="postalCode").text.strip()
#
#         #print(zipcode)
#         nationalsitelist.append( NationalSite(park_type, park_name, park_description, address, city, state, zipcode, closerlookurl))
#
#     #print(data)
#     return nationalsitelist
# #get_sites_for_state("mi")
get_following_info()


#Creating the DB
DBNAME = 'following.db'
FOLLOWING_DATA = 'cache_data.json'

#open json file
fref= open(FOLLOWING_DATA, 'r', encoding ='utf8')
contents=fref.read()
following_data=json.loads(contents)
fref.close()



#create Table
def init_db_json():
    conn = sqlite3.connect(DBNAME)
    cur=conn.cursor()



    statement='''
        DROP TABLE IF EXISTS 'Following_Info';
        '''
    cur.execute(statement)
    statement='''
        DROP TABLE IF EXISTS 'Mutual_Followers';
        '''
    cur.execute(statement)
    conn.commit()

    statement='''
        CREATE TABLE 'Following_Info' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Name' TEXT NOT NULL,
            'Username' TEXT NOT NULL,
            'Bio' TEXT,
            'PostCount' INTEGER NOT NULL,
            'FollowingStudentsofUmich' TEXT NOT NULL

        );
    '''
    cur.execute(statement)


    statement='''
        CREATE TABLE 'Mutual_Followers'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Username' TEXT NOT NULL,
            'FirstName' TEXT NOT NULL,
            'FollowerCount' INTEGER NOT NULL,
            'PostCount' INTEGER NOT NULL

        );
    '''
    cur.execute(statement)
    conn.commit()
    conn.close()

init_db_json()
