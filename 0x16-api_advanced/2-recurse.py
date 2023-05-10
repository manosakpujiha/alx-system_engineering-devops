#!/usr/bin/python3
""" Module - 0-gather_data_from_an_API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""

    headers = {'User-Agent': 'DiegoOrejuela'}
    params = {"limit": 100, 'after': after}
    response = requests.get("https://www.reddit.com/r/{}/hot/.json".
                            format(subreddit), headers=headers, params=params)
    if response:
        after = response.json().get("data").get("after")
        if after:
            recurse(subreddit, hot_list, after=after)
            titles = response.json().get("data").get("children")
            for title in titles:
                hot_list.append(title.get("data").get("title"))
            return(hot_list)
        else:
            titles = response.json().get("data").get("children")
            for title in titles:
                hot_list.append(title.get("data").get("title"))
            return(hot_list)
    else:
        return(None)
