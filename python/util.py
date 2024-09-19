import requests
def search_duckduckgo(query) :
    url ="https://api.duckduckgo.com/"
    params={
        "q" : query,
        "format" : "json",
        "pretty" : 1
    }
    response = requests.get(url, params=params)
    if response.status_code== 200:
        return response.json()
    else:
        return None

