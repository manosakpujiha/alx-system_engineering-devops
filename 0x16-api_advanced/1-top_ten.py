#!/usr/bin/python3
""" Module - 0-gather_data_from_an_API"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""

    headers = {'User-Agent': 'DiegoOrejuela'}
    response = requests.get("https://www.reddit.com/r/{}/hot/.json".
                            format(subreddit), headers=headers)

    if response:
        children = response.json().get("data").get("children")
        for i in range(10):
            print(children[i].get("data").get("title"))
    else:
        print(None)
