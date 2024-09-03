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


def test_getUsers(get_token):
    token = get_token
    headers = {'x-access-token': token}
    usersURL = baseUrl + userURLpath
    res_users = getApiData(usersURL, headers)
    print(json.dumps(res_users.json(), indent=4))
    assert res_users.json()['users'][0]['email']
