#!/usr/bin/python3
""" grt thr number of subs"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for the given subreddit.

    :param subreddit: A string representing the name of the subreddit.
    :return: An integer representing the number of subscribers for the given
    subreddit, or 0 if the subreddit is invalid.
    """

    # Set the URL to query for the subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent header to avoid a 429 Too Many Requests error
    headers = {"User-Agent": "My Reddit Client"}

    # Query the subreddit information from the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the query was successful, extract the number
    # of subscribers from the response
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get("data").get("subscribers")
        return subscribers

    # If the subreddit is invalid, return 0
    else:
        return 0
