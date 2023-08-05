from googlesearch import search
from scr.helpers import get_domain
import requests


def get_google_results(query: str) -> list:
    cards = []
    engine_name = "Google"
    try:
        dips = search(query, advanced=True)
        cards += [{
            'engine': engine_name,
            'title': dip.title,
            'url': dip.url,
            'channel_name': get_domain(dip.url),
            'channel_url': get_domain(dip.url),
            'body': dip.description
        } for dip in dips]
    except requests.exceptions.HTTPError:
        print("{}-Too Many Requests\n".format(engine_name))
    return cards
