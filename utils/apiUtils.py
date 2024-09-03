import requests, json


def getApiData(url, opHeader=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.get(url, verify=False, headers=headers)
    print("RequestURL:" + url)
    print("request header", response.request.headers)
    print("response header", response.headers)
    return response


def DeleteApiData(url, opHeader=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.get(url, verify=False, headers=headers)
    print("RequestURL:" + url)
    print("request header", response.request.headers)
    print("response header", response.headers)
    return response


def putData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("RequestURL" , url)
    print("ReqBody", json.dumps(body))
    response = requests.put(url, verify=False, json=body, headers=headers)
    print("RequestURL:" + url)
    print("request header", response.request.headers)
    print("response header", response.headers)
    return response

def postApiData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("RequestURL", url)
    print("ReqBody", json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers)

