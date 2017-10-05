import requests
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth
from <pyhtonfile> import BASE_URL # BASE_URL is the URL for which is the URL to application, stored in a common file to be able to accessed repeatedly and easily
import os #The credentials are rather stored as system variables

def authenticate():
    """
    Get Token for authentication
    :return: Token
    """
    url = "%s/net2/oauth2/accesstoken.ashx" % BASE_URL
    consumer_key = os.environ['consumer_key']
    response = requests.get(url, auth=HTTPBasicAuth(os.environ['user'], os.environ['password']),
                   headers={'X-ConsumerKey': consumer_key})

    if response.status_code != 200:
        return None
    xml_response = ET.fromstring(response.text)
    for token_tag in xml_response.findall('Token'):
        if token_tag.text:
            token = token_tag.text
            return token



