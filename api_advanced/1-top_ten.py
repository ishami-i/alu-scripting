#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyUserAgent/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
