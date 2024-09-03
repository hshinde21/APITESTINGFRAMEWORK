# import requests, json
# from assertpy import assert_that
#
#
# # get API call and return response data
# def getAPIData(url):
#     headers = {'Content-Type': 'application/json'}
#     print("RequestURL", url)
#     response =
#     data = response.json()
#     assert (len(data)) > 0, "!!!! empty response !!!!"
#     responseTime: float = response.elapsed.total_seconds()
#     return data, response.status_code, responseTime
#
#
# def putAPIData(url, body):
#     header = {'Content-Type': 'application/json'}
#     print("RequestURL", url)
#     print("Requestbody", json.dumps(body))
#     response = requests.put(url, verify=False, json=body, headers=header)
#     data = response.json()
#     responseTime = response.elapsed.total_seconds()
#     return data,response.status_code, responseTime
