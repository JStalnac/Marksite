import mistletoe
from flask import Flask, send_file

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

epic image (not found)
<img src="/images/dawfrgs"/>

This is a link
<https://github.com/JStalnac/Marksite>

"""

html = mistletoe.markdown(md)

print(html + "\n\n\n")

@app.route("/")
def root():
    return html

@app.route("/images/<image>")
def get_image(image):
    return send_file(image, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
