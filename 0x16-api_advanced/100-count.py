import requests
from collections import defaultdict

def count_words(subreddit, word_list, after='', counts=None):
    if counts is None:
        counts = defaultdict(int)  # Initialize counts dictionary if not provided
    
    headers = {"User-Agent": "python:subreddit.wordcounter:v1.0 (by /u/YourUsername)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check for invalid subreddit (status code 302 for redirect or 404 for not found)
    if response.status_code in [302, 404]:
        return
    
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    after = data.get("data", {}).get("after")
    
    for post in posts:
        title = post["data"]["title"].lower()  # Convert title to lowercase
        for word in word_list:
            word_lower = word.lower()
            counts[word_lower] += title.split().count(word_lower)  # Count occurrences of the word
    
    if after is not None:
        # Recursively call the function if there's a next page
        count_words(subreddit, word_list, after, counts)
    else:
        # Sorting and printing the results
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))  # Sort by count desc, then alphabetically
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
