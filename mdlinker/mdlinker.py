import glob
import json


def get_config():
    """returns the config file"""
    with open("mdlinker/config.json") as f:
        return json.load(f)[0]


def get_files():
    """returns a list of all markdown files in the dir structure,
    excluding the readme"""
    exclude = get_config()["exclude"]
    print(exclude)
    mdfiles = glob.glob("**/*.md", recursive=True)
    return [file for file in mdfiles if file.split("/")[-1] not in exclude]
    # return [mdfile for mdfile in mdfiles if mdfile not in exclude]


def get_links(file):
    """returns a list of all links in a file"""
    with open(file) as f:
        return [line.strip() for line in f.readlines() if line.startswith("* [")]


def get_link_categories(file):
    """returns a list of all subject categories in a file path"""
    return file.split("/")[:-1]


def append_link_to_file(link, file):
    """appends a link to a file"""
    with open(file, "a") as f:
        f.write(link + "\n")


def refresh_readme():
    """refreshes the readme file before appending the links"""
    with open("readme.md", "w") as f:
        for line in open("mdlinker/template_readme.md"):
            f.write(line)


if __name__ == "__main__":

    links = get_links("readme.md")

    for path in get_files():
        categories = get_link_categories(path)
        filename = path.split("/")[-1]
        link = f'* [{":".join(categories)}]({path})'

        if link not in links:
            links.append(link)
            print(link)

    refresh_readme()

    for link in sorted(links):
        append_link_to_file(link, "readme.md")
