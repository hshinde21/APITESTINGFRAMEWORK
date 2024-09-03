from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseUrl = getFlaskAppBaseURL()
urlpath = '/allusercount'


def test_getAllUserCountStatus200():
    url = baseUrl + urlpath
    headers = {'Content-Type': 'application/json'}
    resp = getApiData(url, headers)
    assert resp.status_code == 200


def test_getAllUserCountStatus406():
    url = baseUrl + urlpath
    headers = {'Content-Type': 'application/json'}
    resp = getApiData(url, headers)
    assert resp.status_code == 406
