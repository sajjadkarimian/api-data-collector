import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

def save_posts(posts):
    inserted_count = 0

    with psycopg.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "5432"))
) as connection:

        with connection.cursor() as cursor:
            for post in posts:
                cursor.execute(
                    """
                    INSERT INTO posts (id, user_id, title, body)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING
                    """,
                    (
                        post["id"],
                        post["userId"],
                        post["title"],
                        post["body"]
                    )
                )

                inserted_count += cursor.rowcount

    return inserted_count
