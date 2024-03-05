#!/usr/bin/python3
"""
T02
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function Implementation
    """
    base_url = "https://www.reddit.com"
    headers = {"User-Agent": "Chrome/122.0.6261.70 by RobbairBadeia"}

    url = f"{base_url}/r/{subreddit}/hot.json?limit=25"
    if after:
        url += f"&after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for invalid subreddit
    # status code 302 for redirect or 404 for not found
    if response.status_code in [302, 404]:
        return None

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        return hot_list if hot_list else None

    hot_list.extend([post["data"]["title"] for post in posts])

    # Check if there's a next page
    after = data.get("data", {}).get("after", None)
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
