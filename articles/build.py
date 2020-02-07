import os
import sys
import toml

def build_page(name):
    if not os.path.isdir(name):
        raise Exception(f"No page named '{name}'")
    else:
        os.chdir(name)
        page_data = toml.load("page.cfg")
        print(page_data)

if __name__ == "__main__":
    if len(sys.argv) == 0:
        raise ValueError("Page name not defined!")
    name = sys.argv[1]

    print(f"Building page '{name}'...")
    build_page(name)
