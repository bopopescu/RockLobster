import requests
import json
from requests.exceptions import HTTPError

http_response = {
		"headers": {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"},
	    "isBase64Encoded": False,
	    "statusCode": 200,
	    "body": ""
	}

autoresponse_header = "Welcome to Paddle support! One of our agents will get back to you shortly. In the meantime, take a look at the following article: "

swiftype_engine_urls = {
    "faq": "https://search-api.swiftype.com/api/v1/engines/paddle-faq/search.json",
    "documentation": "https://search-api.swiftype.com/api/v1/engines/paddle-documentation/search.json",
    "blog": "https://search-api.swiftype.com/api/v1/engines/paddle-blog/search.json",
    "developer": "https://search-api.swiftype.com/api/v1/engines/paddle-developer/search.json",
}

swiftype_call_params = {
    "auth_token": "6oMTu5o6HVtFMPjbHTDJ",
    "q": "Welcome to Paddle!"
}

def call_swiftype_search(url):
    response = requests.get(url, swiftype_call_params)
    return response.content

def main_lookup(event, context):
    message_body = event['queryStringParameters']
    swiftype_call_params["q"] = message_body['message']
    swiftype_response = json.loads(call_swiftype_search(swiftype_engine_urls["faq"]))
    return_string = autoresponse_header + swiftype_response["records"]["page"][0]["title"] + " " + swiftype_response["records"]["page"][0]["url"]
    http_response["body"] = return_string
    print(http_response)
    return http_response
