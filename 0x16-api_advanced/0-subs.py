#!/usr/bin/python3
""" Module - 0-gather_data_from_an_API"""

import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0."""
    headers = {'User-Agent': 'DiegoOrejuela'}
    response = requests.get("https://www.reddit.com/r/{}/about.json".
                            format(subreddit), headers=headers)

    if response:
        return(response.json().get("data").get("subscribers"))
    else:
        return(0)
