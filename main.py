import requests
from requests.exceptions import HTTPError

inbound_urlcall_from_kustomer = "http://webhook.site/2f8dcb04-ce40-493b-b8c5-30570bb2fa2e?message=What%20happened%20to%20my%20payout%3F"
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


def get_message_from_kustomer_call(event, context):
    # body = event['queryStringParameters']
    swiftype_call_params["q"] = body['message']



def call_swiftype_search(url):
    response = requests.get(url, swiftype_call_params)
    return response.content

print(call_swiftype_search("https://search-api.swiftype.com/api/v1/engines/paddle-faq/search.json"))