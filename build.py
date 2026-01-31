import os
import shutil
import pandoc
import time

from frontmatter import Frontmatter
from pathlib import Path


OUTPUT_DIRECTORY = os.getenv("BUILD_DIR", "public/")
POST_SNIPPET = """
<div>
    <a href="/{posts_directory_name}/{slug}/"><h3>{title}</h3></a>
    <div class="subtext">{date}</div>
</div>
"""
WIKI_POST_SNIPPET = """
<div class="garden-section-header">
  <h3>
    <a href="/wiki-pages/{slug}">{title}</a>
  </h3>
</div>
<br>
"""

def build_wiki(content_title: str, content_description: str,
               posts_directory_name: str):
    # Load wiki template.
    with open(f"src/templates/wiki-template.html", "r") as file:
        post_template = file.read()

    posts_directory_path = Path(f"src/wiki-pages")
    post_titles = []
    post_html_snippets = []
    wiki_docs = []
    for file in posts_directory_path.glob("*.md"):
        slug = Path(file).stem

        # Read the frontmatter to get wiki type and title
        post = Frontmatter.read_file(file)
        title = post["attributes"]["title"]
        wiki_type = post["attributes"].get("wikiType", None)

        # Only include "parent" wiki pages in the index.
        if wiki_type == "parent":
            post_titles.append(title)
            # Generate the HTML snippet for this post's link on the blog index.
            post_html_snippets.append(
                WIKI_POST_SNIPPET.format(slug=slug, title=title)
            )

        # Convert the doc to HTML with Pandoc.
        doc = pandoc.read(source=post["body"], format="markdown")
        formatted_content = pandoc.write(doc, format="html")
        post_html = post_template.format(
            title=title,
            content=formatted_content,
        )

        # Write the formatted post to the output directory.
        post_path = os.path.join(OUTPUT_DIRECTORY, posts_directory_name, slug)
        os.makedirs(post_path, exist_ok=True)
        with open(os.path.join(post_path, "index.html"), "w") as file:
            file.write(post_html)

    # Sort the post snippets by ascending title.
    sorted_pairs = sorted(zip(post_titles, post_html_snippets), key=lambda
                          pair: pair[0])
    sorted_snippets = [pair[1] for pair in sorted_pairs]

    # Write the wiki index HTML.
    with open("src/wiki-index.html", "r") as file:
        index_template = file.read()
    index_html = index_template.format(content_title=content_title,
                                       content_description=content_description,
                                       posts=str.join("\n", sorted_snippets))
    with open(os.path.join(OUTPUT_DIRECTORY, posts_directory_name, "index.html"), "w") as file:
        file.write(index_html)

def build_content_site(content_title: str, content_description: str,
                       posts_directory_name: str):
    # Load post template.
    with open("src/templates/post-template.html", "r") as file:
        post_template = file.read()

    posts_directory_path = Path(f"src/{posts_directory_name}/posts")
    post_dates = []
    post_html_snippets = []
    for file in posts_directory_path.glob("*.md"):
        slug = Path(file).stem

        # Read the frontmatter to get the title and date
        post = Frontmatter.read_file(file)
        title = post["attributes"]["title"]
        date = post["attributes"]["date"]
        # Convert the doc to HTML with Pandoc.
        doc = pandoc.read(source=post["body"], format="markdown")
        formatted_content = pandoc.write(doc, format="html")
        post_html = post_template.format(
            title=title,
            date=date.strftime("%B %d, %Y"),
            posts_directory_name=posts_directory_name,
            content_title=content_title,
            content=formatted_content,
        )

        # Generate the HTML snippet for this post's link on the blog index.
        post_html_snippets.append(
            POST_SNIPPET.format(posts_directory_name=posts_directory_name,
                                slug=slug, title=title,
                                date=date.strftime("%B %d, %Y")),
        )
        post_dates.append(date)

        # Write the formatted post to the output directory.
        post_path = os.path.join(OUTPUT_DIRECTORY, posts_directory_name, slug)
        os.makedirs(post_path, exist_ok=True)
        with open(os.path.join(post_path, "index.html"), "w") as file:
            file.write(post_html)

    # Sort the post snippets by descending date.
    sorted_pairs = sorted(zip(post_dates, post_html_snippets), reverse=True)
    sorted_snippets = [pair[1] for pair in sorted_pairs]

    # Write the blog index HTML.
    with open("src/blog-index.html", "r") as file:
        index_template = file.read()
    index_html = index_template.format(content_title=content_title,
                                       content_description=content_description,
                                       posts=str.join("\n", sorted_snippets))
    with open(os.path.join(OUTPUT_DIRECTORY, posts_directory_name, "index.html"), "w") as file:
        file.write(index_html)


def build():
    # This script writes output to the public/ directory. If the directory exists,
    # delete it.
    start = time.perf_counter()
    if os.path.exists(OUTPUT_DIRECTORY):
        shutil.rmtree(OUTPUT_DIRECTORY)

    # Copy src/static to public/.
    shutil.copytree("src/static/", OUTPUT_DIRECTORY)

    build_content_site(content_title="The Strays",
                       content_description="The home of John Mathena's stray thoughts",
                       posts_directory_name="the-strays")
    build_content_site(content_title="Droppin Dimes",
                       content_description="ludirous lyrical mastery",
                       posts_directory_name="droppin-dimes")
    build_wiki(content_title="John's Digital Garden",
               content_description="The place where I store the stuff my brain swears I'll come back to later",
               posts_directory_name="wiki-pages"),
    elapsed = time.perf_counter() - start
    print(f"Site build complete! ({elapsed:.2f} seconds)")


if __name__ == "__main__":
    build()
