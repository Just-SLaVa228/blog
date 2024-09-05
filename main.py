from flask import Flask, render_template
import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/categories")
def category_list():
    return render_template("category_lists.html", category_list=db.get_categories())

@app.route("/posts")
def post_list():
    return render_template("posts_lists.html", post_list=db.get_pos())

@app.route("/category/<id>")
def PosByCategory(id):
    return render_template("posts_lists.html", post_list=db.get_PosByCategory(id))

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")