
import requests


def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    posts = response.json()

    return posts
