from database.db_init import DatabaseConnection

if __name__ == "__main__":
    print("this is not supposed to be ran standalone!!")
    exit()


def create_table() -> None:
    with DatabaseConnection("posts.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS posts(post_id integer primary key, title text, content text)"
        )


def add(post_id: int, title: str, content: str):
    with DatabaseConnection("posts.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO posts VALUES(?,?,?)", (post_id, title, content))


def delete(post_id):
    with DatabaseConnection("posts.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM posts WHERE post_id=?", (post_id,))


def list_posts():
    with DatabaseConnection("posts.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = [
            {"post_id": row[0], "title": row[1], "content": row[2]} for row in cursor.fetchall()
        ]
    return posts
