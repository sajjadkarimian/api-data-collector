
def find_new_posts(incoming_posts, existing_ids):
    new_posts = []

    for post in incoming_posts:
        if post["id"] not in existing_ids:
            new_posts.append(post)
            existing_ids.add(post["id"])

    return new_posts
