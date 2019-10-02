import requests
from requests.exceptions import HTTPError


swiftype_engine_search_query = "checkout"

swiftype_engine_urls = {
    "faq": "https://search-api.swiftype.com/api/v1/engines/paddle-faq/search.json",
    # "documentation": "https://search-api.swiftype.com/api/v1/engines/paddle-documentation/search.json",
    # "blog": "https://search-api.swiftype.com/api/v1/engines/paddle-blog/search.json",
    # "developer": "https://search-api.swiftype.com/api/v1/engines/paddle-developer/search.json",

}

swiftype_call_params = {
    "auth_token": "6oMTu5o6HVtFMPjbHTDJ",
    "q": swiftype_engine_search_query
}

def call_swiftype_search(url):
    response = requests.get(url, swiftype_call_params)
    return response

