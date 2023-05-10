#!/usr/bin/python3

'''recurse the function'''

import requests


def recurse(subreddit, hot_list=[], after=""):

    url = "https://www.reddit.com/r/{}/hot.json?limit=50".format(subreddit)
    if after:
        url += "&after=" + after
    headers = {"User-Agent": "My agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            hot_list.append(post['data']['title'])

        after = posts['data']['after']
        if after:
            recurse(subreddit, hot_list=hot_list, after=after)

        return hot_list
    else:
        return None
