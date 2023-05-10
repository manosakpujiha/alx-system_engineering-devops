#!/usr/bin/python3
"""A file to make a query to an endpoint"""
from requests import request


def count_words(subreddit, word_list, after=None, counts=None):
    # If it's the first call, initialize counts dictionary
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    # Build the API endpoint URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}
    if after is not None:
        params["after"] = after

    # Query the API and check for errors
    response = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        print(f"Error {response.status_code} querying subreddit {subreddit}")
        return

    # Parse the JSON response and extract titles
    data = response.json()
    titles = [post["data"]["title"].lower() for post in data["data"]["children"]]

    # Count the occurrences of each keyword in the titles
    for title in titles:
        words = title.split()
        for word in words:
            word = word.strip(".!_")
            if word.lower() in counts:
                counts[word.lower()] += 1

    # Check if there are more posts to query
    if data["data"]["after"] is not None:
        count_words(subreddit, word_list, after=data["data"]["after"], counts=counts)
    else:
        # Print the results sorted by count and alphabetically
        results = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for result in results:
            if result[1] > 0:
                print(f"{result[0]}: {result[1]}")
