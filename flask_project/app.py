from database import db
from flask import Flask, render_template, request, redirect, url_for

import os


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", posts=db.list_posts())


@app.route("/post/<int:post_id>")
def get_posts(post_id):
    posts = [post for post in db.list_posts()]
    if not posts[post_id]:
        return render_template("404.html", message=f"A post with id {post_id} was not found")
    return render_template("posts.html", post=posts[post_id], post_id=post_id)


@app.route("/post/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post_id = len(db.list_posts())
        if not title or not content:
            return render_template("404.html", message="incorrect data ")
        db.add(post_id, title, content)

        return redirect(url_for("get_posts", post_id=post_id))
    return render_template("form.html")


def main():
    if not os.path.isfile("../posts.db"):
        print("database not found.. creating one")
        db.create_table()
    else:
        print("database found")


if __name__ == "__main__":
    main()
    app.run(debug=True)
