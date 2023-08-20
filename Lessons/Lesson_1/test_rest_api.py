"""https://www.mediawiki.org/wiki/API:Geosearch"""

import requests

S = requests.Session()


def get_sizes(lat, long, radius, limit=100):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }

    r = S.get(url=url, params=params)
    pages = r.json()
    places = pages['query']['geosearch']

    return [i['title'] for i in places]


def test_step1(coordinates, text):
    assert text in get_sizes(coordinates[0], coordinates[1], 100), 'Not found'