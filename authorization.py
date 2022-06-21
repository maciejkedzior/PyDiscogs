from requests_oauthlib import OAuth1Session, OAuth1


CLIENT_KEY = 'uVRZZXYKWHqqPprvFftJ'
CLIENT_SECRET =	'gqOvioXJkjdowLzDKLMHHQTlcBECEYPF'
REQUEST_TOKEN_URL = 'https://api.discogs.com/oauth/request_token'
BASE_AUTHORIZATION_URL = 'https://www.discogs.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://api.discogs.com/oauth/access_token'

class Authorization:
    def __init__(self) -> OAuth1Session:
        first_oauth = OAuth1Session(client_key=CLIENT_KEY, client_secret=CLIENT_SECRET)
        fetch_response = first_oauth.fetch_request_token(REQUEST_TOKEN_URL)

        resource_owner_key = fetch_response.get('oauth_token')
        resource_owner_secret = fetch_response.get('oauth_token_secret')

        authorization_url = first_oauth.authorization_url(BASE_AUTHORIZATION_URL)
        print('Please go here and authorize,', authorization_url)
        verifier = input('Please input the verifier: ')

        oauth = OAuth1Session(CLIENT_KEY,
                                client_secret=CLIENT_SECRET,
                                resource_owner_key=resource_owner_key,
                                resource_owner_secret=resource_owner_secret,
                                verifier=verifier)

        oauth_tokens = oauth.fetch_access_token(ACCESS_TOKEN_URL)


        resource_owner_key = oauth_tokens.get('oauth_token')
        resource_owner_secret = oauth_tokens.get('oauth_token_secret')
        self.oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret)