import requests

SESSION = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"


def search(word: str) -> str:
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": word
    }

    req = SESSION.get(url=URL, params=params)
    data = req.json()

    if data['query']['search'][0]['title'] == word:
        query = data['query']['search'][0]['snippet']
        query = query.replace("<span class=\"searchmatch\">", "")
        query = query.replace("</span>", "")
        return query

    return "I could not found any information, sir."
