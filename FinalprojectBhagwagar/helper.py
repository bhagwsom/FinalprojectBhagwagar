import json

import requests

import secrets


def get_musictest(q, mtype='album'):
    client_key = secrets.client_key
    client_secret = secrets.client_secret

    grant_type='client_credentials'

    body_params={'grant_type':grant_type}
    #Code for OAuth starts
    url = 'https://accounts.spotify.com/api/token'
    #auth = OAuth1(client_key, client_secret)
    resp=requests.post(url, data=body_params, auth= (client_key, client_secret))
    # resp=requests.post(url, headers={'Authorization' : 'Basic ' + client_key + ':' +client_secret},
    # data={'grant_type':'client_credentials'})
    json_resp=json.loads(resp.text)
    token=json_resp['access_token']
    data=requests.get("https://api.spotify.com/v1/search", headers={"Authorization": "Bearer " +token}, params={"type":mtype, 'q':q})#requests.get('https://api.spotify.com/v1/albums/0sNOF9WDwhWunNAHPD3Baj', headers={'authorization': 'Bearer' + token})
    #print(data.text)
    return data
test=get_musictest(q="Chris Brown", mtype='artist')
print(test.text)
