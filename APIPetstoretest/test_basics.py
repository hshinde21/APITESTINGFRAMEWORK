import requests, json
import  logging
from assertpy import assert_that

from utils.myconfigparser import getPetAPIURL
from utils.myutils import getAPIData, putAPIData
Logging = logging.getLogger(__name__)
petID = '31'
baseURI = getPetAPIURL()


# # testing valid response or response in empty
def test_getPetById_response():

    url = baseURI + petID
    data, status, timeTaken = getAPIData(url)
    # assert_that(data['name']).is_equal_to('mitch')
    assert_that(status).is_equal_to(200)
    Logging.info("testcase started for the get api")
    print("response time of the api", timeTaken)


# def test_getPetById_id():
#     url = baseURI + petID
#     header = {'Content-Type': 'application/json'}
#     print("RequestURL", url)
#     response = requests.get(url, verify=True, headers=header)
#     data = response.json()
#     # python assertion
#     # assert data['id'] == 21, "id verified"
#     # fluent assertion
#     assert_that(data['id']).is_equal_to(21)

def test_updatingPet():
    payload = {"id": int(petID), "name": "mitch", "status": "WIP"}

    data, status, timeTaken = putAPIData(baseURI, payload)
    assert data['id'] == petID
    assert_that(status).is_equal_to(200)
