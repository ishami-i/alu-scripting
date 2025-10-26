#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries Reddit and prints the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except Exception:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
    except Exception:
        print(None)
        return

    posts = data.get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
