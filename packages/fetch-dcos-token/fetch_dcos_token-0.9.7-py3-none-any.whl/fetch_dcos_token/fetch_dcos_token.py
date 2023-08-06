import json
import requests
import datetime
import jwt
import warnings
warnings.filterwarnings("ignore")


def getjwt(cluster, username, userkey):
    keyfile = open(userkey, "r")
    private_key = keyfile.read()
    thetoken = jwt.encode(
        {"uid": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)},
        private_key, algorithm='RS256'
    )
    logintoken = thetoken.decode("utf-8")
    headers = {'Content-Type': 'application/json'}
    theusername = '"' + username + '"'
    thelogintoken = '"' + logintoken + '"'
    thepayload = '{"uid": ' + theusername + ', ' + '"token" :' + thelogintoken + '}'

    payload = thepayload
    api_endpoint = '/acs/api/v1/auth/login'
    api = cluster + api_endpoint

    tokenreturn = requests.post(url=api, headers=headers, data=payload, verify=False)
    token_dict = json.loads(tokenreturn.text)
    return token_dict['token']

