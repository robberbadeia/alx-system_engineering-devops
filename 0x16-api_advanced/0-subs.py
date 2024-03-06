#!/usr/bin/python3
"""
T00
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function Implementation
    """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    results = res.json().get('data')
    return results.get('subscribers')
