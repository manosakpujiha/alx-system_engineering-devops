#!/usr/bin/python3
"""find the top ten"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for the given subreddit.

    :param subreddit: A string representing the name of the subreddit.
    """

    # Set the URL to query for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent header to avoid a 429 Too Many Requests error
    headers = {"User-Agent": "My Reddit Client"}

    # Query the subreddit's hot posts from the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the query was successful, print the titles of the first 10 hot posts
    if response.status_code == 200:
        data = response.json().get("data")
        for post in data.get("children")[:10]:
            title = post.get("data").get("title")
            print(title)

    # If the subreddit is invalid, print None
    else:
        print(None)
