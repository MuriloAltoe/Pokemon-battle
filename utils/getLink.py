import requests

def getJSON(link):
    res = requests.get(link)
    json = res.json()

    return json