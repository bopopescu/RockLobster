import requests
import json
from requests.exceptions import HTTPError

test_event = {'resource': '/kustomer_chat_knowledgebase_lookup', 'path': '/kustomer_chat_knowledgebase_lookup', 'httpMethod': 'POST', 'headers': {'Content-Type': 'application/json', 'Host': '97niwo5cfe.execute-api.us-east-2.amazonaws.com', 'X-Amzn-Trace-Id': 'Root=1-5d95ea56-076f230581dec7bbe1071d7c', 'x-datadog-parent-id': '5934599936870363752', 'x-datadog-sampling-priority': '0', 'x-datadog-trace-id': '5373981340826849292', 'X-Forwarded-For': '52.70.7.21', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Content-Type': ['application/json'], 'Host': ['97niwo5cfe.execute-api.us-east-2.amazonaws.com'], 'X-Amzn-Trace-Id': ['Root=1-5d95ea56-076f230581dec7bbe1071d7c'], 'x-datadog-parent-id': ['5934599936870363752'], 'x-datadog-sampling-priority': ['0'], 'x-datadog-trace-id': ['5373981340826849292'], 'X-Forwarded-For': ['52.70.7.21'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': {'message': 'This is the print event test'}, 'multiValueQueryStringParameters': {'message': ['This is the print event test']}, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'jk49ax', 'resourcePath': '/kustomer_chat_knowledgebase_lookup', 'httpMethod': 'POST', 'extendedRequestId': 'A_GNjGSdiYcFTpQ=', 'requestTime': '03/Oct/2019:12:32:22 +0000', 'path': '/default/kustomer_chat_knowledgebase_lookup', 'accountId': '493031189710', 'protocol': 'HTTP/1.1', 'stage': 'default', 'domainPrefix': '97niwo5cfe', 'requestTimeEpoch': 1570105942639, 'requestId': '2a1294cd-55d9-4db0-a532-2cfe8091c3ae', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '52.70.7.21', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': None, 'user': None}, 'domainName': '97niwo5cfe.execute-api.us-east-2.amazonaws.com', 'apiId': '97niwo5cfe'}, 'body': '{"message":"Hello World!","initialMessage":"Test","kustomerConversation":"initialMessage"}', 'isBase64Encoded': False}

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

    # swiftype_call_params["q"] = message_body['message']  <- Uncomment for production   !!!!!!!

    swiftype_response = json.loads(call_swiftype_search(swiftype_engine_urls["faq"]))
    return_string = autoresponse_header + swiftype_response["records"]["page"][0]["title"] + " " + swiftype_response["records"]["page"][0]["url"]
    print(return_string)
    return return_string


main_lookup(test_event, "context")