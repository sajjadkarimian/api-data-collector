
from api_client import fetch_posts
from db import save_posts

posts = fetch_posts()


print("Total fetched posts:", len(posts))
print("First post ID:", posts[0]["id"])

inserted_count = save_posts(posts)
print("Posts inserted into database:", inserted_count)
