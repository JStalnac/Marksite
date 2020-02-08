import os
import sys
import toml
def make_page(name):
    if not os.path.isdir(name):
        os.mkdir(name)
        os.chdir(name)

        page_data = {"title": "New Page", "authors": ["None"] }

        with open("page.cfg", "w+") as f:
            toml.dump(page_data, f)
            f.close()

        with open("page.md", "w+") as f:
           f.write("""# New Article\nFor help with markdown read the [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)""")

    else:
        raise Exception(f"Page by the name '{name}' already exists!")

if __name__ == "__main__":
    if len(sys.argv) == 0:
        raise ValueError("Page name not defined!")

    name = sys.argv[1]
    make_page(name)
    print(f"Created article with name '{name}'")
