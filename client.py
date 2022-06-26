from urllib import response
from requests_oauthlib import OAuth1Session, OAuth1
from user import User
import requests
import json


BASE_URL = 'https://api.discogs.com'
REQUEST_TOKEN_URL = BASE_URL + '/oauth/request_token'
BASE_AUTHORIZATION_URL = 'https://www.discogs.com/oauth/authorize'
ACCESS_TOKEN_URL = BASE_URL + '/oauth/access_token'


class Client:
    def __init__(self, client_key=None, client_secret=None):
        if client_key is None or client_secret is None:
            raise ValueError("Empty client key or client secret")
        
        first_oauth = OAuth1Session(client_key=client_key, client_secret=client_secret)
        fetch_response = first_oauth.fetch_request_token(REQUEST_TOKEN_URL)

        resource_owner_key = fetch_response.get('oauth_token')
        resource_owner_secret = fetch_response.get('oauth_token_secret')

        authorization_url = first_oauth.authorization_url(BASE_AUTHORIZATION_URL)
        print('Please go here and authorize,', authorization_url)
        verifier = input('Please input the verifier: ')
        
        oauth = OAuth1Session(client_key,
                                client_secret=client_secret,
                                resource_owner_key=resource_owner_key,
                                resource_owner_secret=resource_owner_secret,
                                verifier=verifier)

        oauth_tokens = oauth.fetch_access_token(ACCESS_TOKEN_URL)
        resource_owner_key = oauth_tokens.get('oauth_token')
        resource_owner_secret = oauth_tokens.get('oauth_token_secret')

        self.oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret)

    def verify_identity(self):
        response = requests.get(url=BASE_URL + '/oauth/identity', auth=self.oauth)
        response.raise_for_status()
        return json.loads(response.text)


    def get_release():
        pass

    def get_user_by_username(self, username: str) -> User:
        response = requests.get(url=BASE_URL + '/users/{}'.format(username), auth=self.oauth)
        response.raise_for_status()
        return User(json.loads(response.text))