#!/usr/bin/python3
"""Recurse function"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for the given subreddit.

    :param subreddit: A string representing the name of the subreddit.
    :param hot_list: A list containing the titles of hot articles.
    Defaults to an empty list.
    :param after: A string representing the ID of the last post
    in the current page of results.
                  Defaults to None.
    :return: A list containing the titles of all hot
    articles for the given subreddit.
             Returns None if no results are found for the given subreddit.
    """

    # Set the URL to query for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=50".format(subreddit)

    # Set a custom User-Agent header to avoid a 429 Too Many Requests error
    headers = {"User-Agent": "My Reddit Client"}

    # Query the subreddit's hot posts from the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the query was successful, add the titles of the posts to the hot_list
    if response.status_code == 200:
        articles = response.json()

        for article in articles['data']['children']:
            hot_list.append(article['data']['title'])

        url = url + '&after=' + articles['data']['after']
    else:
        return None

    return hot_list
