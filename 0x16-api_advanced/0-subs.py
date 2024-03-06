#!/usr/bin/python3
"""
T00
"""
import requests
from requests import *


def number_of_subscribers(subreddit):
    """
    Function Implementation
    """
    client_id = 'xnDxd-7qr-aFwHQ7_k-kKw'
    client_secret = '4KVZ5lw12yu3KYQZ8ytXZb0ejaShQQ'
    user_agent = 'Chrome/122.0.6261.95'

    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    headers = {'User-Agent': user_agent}
    data = {'grant_type': 'password',
            'username': 'RobbairBadeia',
            'password': 'Godislove'}
    auth_url = 'https://www.reddit.com/api/v1/access_token'

    # Get OAuth token
    token_response = requests.post(auth_url,
                                   auth=auth,
                                   data=data,
                                   headers=headers)
    token = token_response.json().get('access_token')

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': user_agent}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    results = res.json().get('data')
    return results.get('subscribers')
