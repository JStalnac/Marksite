import mistletoe
from flask import Flask, send_file, render_template

app = Flask(__name__)

md = """
# Title
## Subtitle
text
## Another subtitle
more text

even more text

```python
print("Python code")
```

This is a link
<https://github.com/JStalnac/Marksite>
This is a hyperlink
[Google](https://google.co.uk/)

"""

html = mistletoe.markdown(md)

# print(html + "\n\n\n")

@app.route("/")
def root():
    return html

@app.route("/images/<image>")
def get_image(image):
    return send_file(image, mimetype="image/png")

@app.route("/article/<name>/")
def article(name):
    return render_template("article.html", content=name)

if __name__ == "__main__":
    app.run(debug=True)
