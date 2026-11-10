
from post_utils import find_new_posts


def test_find_new_posts():

    existing_ids = {1, 2, 3}

    incoming_posts = [
        {"id": 2, "title": "Existing post"},
        {"id": 4, "title": "New post A"},
        {"id": 5, "title": "New post B"}
    ]

    result = find_new_posts(incoming_posts, existing_ids)

    assert len(result) == 2
    assert result[0]["id"] == 4
    assert result[1]["id"] == 5


def test_duplicate_in_same_batch():

    existing_ids = {1, 2, 3}

    incoming_posts = [
        {"id": 6, "title": "New post A"},
        {"id": 6, "title": "New post A duplicate"}
    ]

    result = find_new_posts(incoming_posts, existing_ids)

    assert len(result) == 1
    assert 6 in existing_ids


