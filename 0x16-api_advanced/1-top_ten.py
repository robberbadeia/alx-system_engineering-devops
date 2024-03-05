#!/usr/bin/python3
"""
T01
"""
import requests


def top_ten(subreddit):
    """
    Function Imo=plementation
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        "User-Agent": "python:reddit.top.ten:v1.0 (by /u/RobbairBadeia)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for invalid subreddit
    # status code 302 for redirect or 404 for not found
    if response.status_code in [302, 404]:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print(None)
    else:
        for post in posts:
            print(post["data"]["title"])
