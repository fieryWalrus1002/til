import glob
import json

LINK_SPLIT = ":  "

def get_config():
    """returns the config file"""
    with open("mdlinker/config.json") as f:
        return json.load(f)[0]


def get_files():
    """returns a list of all markdown files in the dir structure,
    excluding the readme files in the config file"""
    exclude = get_config()["exclude"]
    mdfiles = glob.glob("**/*.md", recursive=True)
    return [file for file in mdfiles if file.split("/")[-1] not in exclude]
    # return [mdfile for mdfile in mdfiles if mdfile not in exclude]


def get_links(file):
    """returns a list of all links in a file"""
    with open(file) as f:
        return [line.split(LINK_SPLIT)[0].strip() for line in f.readlines() if line.startswith("* [")]


def get_header_from_md(file):
    """returns the header from a markdown file"""
    with open(file) as f:
        return f.readline().strip().replace("#", "").strip()

def get_link_categories(file):
    """returns a list of all subject categories in a file path"""
    return file.split("/")[:-1]


def append_to_file(newstr, file):
    """appends a string to a file"""
    with open(file, "a") as f:
        f.write(newstr + "\n")


def refresh_readme():
    """refreshes the readme file before appending the links"""
    with open("readme.md", "w") as f:
        for line in open("mdlinker/template_readme.md"):
            f.write(line)


def reindex_links():
    links = get_links("readme.md")

    for path in get_files():
        categories = get_link_categories(path)
        filename = path.split("/")[-1]
        link = f'* [{":".join(categories)}]({path})'

        if link not in links:
            links.append(link)

    refresh_readme()

    for link in sorted(links):
        header = get_header_from_md(link.split("(")[1].split(")")[0])
        append_to_file(link + LINK_SPLIT + header, "readme.md")


if __name__ == "__main__":
    reindex_links()
