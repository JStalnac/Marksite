import os
import mistletoe
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello!</h1>"

@app.route("/article/<name>/")
def article(name):
    if not os.path.isfile(f"templates/pages/{name}/page.html"):
        return render_template("article.html", content="pages/PageNotFound.html")
    else:
        return render_template("article.html", content=f"pages/{name}/page.html")

if __name__ == "__main__":
    app.run(debug=True)
