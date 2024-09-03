# import token
import token
import logging
LOGGER = logging.getLogger()
from utils.apiUtils import getApiData, postApiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseUrl = getFlaskAppBaseURL()
urlpath = '/login'
registerJsonFile = 'loginvaliduser.json'
userURLpath = 'users'


# def test_registerApi():
#     url = baseUrl + urlpath
#     payload = getJsonFromFile(registerJsonFile)
#     response = postApiData(url, payload)
#     print(response.json())
#     assert response.status_code == 201
#     assert response['id'] == '5'
# 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjEiLCJleHAiOjE3MjUxODUzOTh9.EnZphymm_mpvfOyLt31IsF0lMdi6X-8czVkqu9Udnrg'
# token test

def test_auth_demo():
    url = baseUrl + urlpath
    payload = getJsonFromFile(registerJsonFile)
    response = postApiData(url, payload)
    print(response.json()['token'])
    token = response.json()['token']
    userURL= baseUrl+userURLpath

    headers = {'x-access-token': token}
    res_users = getApiData(userURL, headers)
    LOGGER.debug(res_users)
    print(res_users.json())
