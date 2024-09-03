import pytest
from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseUrl = getFlaskAppBaseURL()
urlpath = '/allusercount'
testData = [
    ('application/json', 200),
    ('application/xml', 406)
]

@pytest.mark.parametrize("type, status", testData)
def test_getAllUserCountStatus200(type, status):
    url = baseUrl + urlpath
    headers = {'Accept': type}
    resp = getApiData(url, headers)
    assert resp.status_code == status
