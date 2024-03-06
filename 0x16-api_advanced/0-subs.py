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
    reddit_username = 'RobbairBadeia'
    reddit_password = 'Godislove'

    auth_url = 'https://www.reddit.com/api/v1/access_token'

    auth_data = {'grant_type': 'password',
                 'username': reddit_username,
                 'password': reddit_password}

    # HTTP basic authentication header with client ID and secret
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    # Make a POST request to obtain access token
    response = requests.post(auth_url,
                             data=auth_data,
                             auth=auth,
                             headers={
                                 'User-Agent': 'Script by /u/RobbairBadeia'})

    if response.status_code == 200:
        access_token = response.json()['access_token']

    # Reddit API endpoint for getting subreddit info
    subreddit_url = f'https://oauth.reddit.com/r/{subreddit}/about.json'

    # Include access token in request headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'User-Agent': 'Script by /u/RobbairBadeia'
    }

    # Make a GET request to fetch subreddit info
    res = requests.get(subreddit_url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        results = res.json().get('data')
        return results.get('subscribers')
    return 0
