import os
import sys
import toml
import mistletoe

def build_page(name):
    if not os.path.isdir(name):
        raise Exception(f"No page named '{name}'")
    else:
        os.chdir(name)
        page_data = toml.load("page.cfg")
        print(page_data)

        if not os.path.isfile("page.md"):
            raise FileNotFoundError("No page markdown file found!")

        with open("page.md") as f:
            md = f.read()
            f.close()

        with open("page.html", "w+") as f:
            html = mistletoe.markdown(md)
            f.write(html)
            f.close()

if __name__ == "__main__":
    if len(sys.argv) == 0:
        raise ValueError("Page name not defined!")
    name = sys.argv[1]

    print(f"Building page '{name}'...")
    build_page(name)
