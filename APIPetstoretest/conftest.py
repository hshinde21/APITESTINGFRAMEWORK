import pytest
import json

import pytest
from utils.apiUtils import getApiData, postApiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = 'loginvaliduser.json'
baseUrl = getFlaskAppBaseURL()
userURLpath = '/users'
loginUrlpath = '/login'



@pytest.fixture()
def get_token():
    try:
        loginURL = baseUrl + loginUrlpath
        payload = getJsonFromFile(loginJsonFile)
        loginResp = postApiData(loginURL, payload)
        print(loginResp.json()['token'])
        token = loginResp.json()['token']
        yield token
    except Exception as e:
        print(e)
