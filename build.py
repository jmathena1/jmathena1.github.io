import os
import shutil
import pandoc

from frontmatter import Frontmatter
from pathlib import Path


OUTPUT_DIRECTORY = os.getenv("BUILD_DIR", "public/")
POST_SNIPPET = """
<div class="post">
    <a href="/the-strays/{slug}/"><h3>{title}</h3></a>
    <div class="subtext">{date}</div>
</div>
"""


def build_blog():
    # Load post template.
    with open("src/the-strays/post-template.html", "r") as file:
        post_template = file.read()

    posts_directory = Path("src/the-strays/posts")
    post_dates = []
    post_html_snippets = []
    for file in posts_directory.glob("*.md"):
        slug = Path(file).stem

        # Read the frontmatter to get the title and date
        post = Frontmatter.read_file(file)
        title = post["attributes"]["title"]
        date = post["attributes"]["date"].strftime("%B %d, %Y")

        # Convert the doc to HTML with Pandoc.
        doc = pandoc.read(source=post["body"], format="markdown")
        formatted_content = pandoc.write(doc, format="html")
        post_html = post_template.format(
            title=title,
            date=date,
            content=formatted_content,
        )

        # Generate the HTML snippet for this post's link on the blog index.
        post_html_snippets.append(
            POST_SNIPPET.format(slug=slug, title=title, date=date)
        )
        post_dates.append(post["attributes"]["date"])

        # Write the formatted post to the output directory.
        post_path = os.path.join(OUTPUT_DIRECTORY, "the-strays", slug)
        os.makedirs(post_path, exist_ok=True)
        with open(os.path.join(post_path, "index.html"), "w") as file:
            file.write(post_html)

    # Sort the post snippets by descending date.
    sorted_pairs = sorted(zip(post_dates, post_html_snippets), reverse=True)
    sorted_snippets = [pair[1] for pair in sorted_pairs]

    # Write the blog index HTML.
    with open("src/the-strays/index-template.html", "r") as file:
        index_template = file.read()
    index_html = index_template.format(posts=str.join("\n", sorted_snippets))
    with open(os.path.join(OUTPUT_DIRECTORY, "the-strays", "index.html"), "w") as file:
        file.write(index_html)


def build():
    # This script writes output to the public/ directory. If the directory exists,
    # delete it.
    if os.path.exists(OUTPUT_DIRECTORY):
        shutil.rmtree(OUTPUT_DIRECTORY)

    # Copy src/static to public/.
    shutil.copytree("src/static/", OUTPUT_DIRECTORY)

    build_blog()


if __name__ == "__main__":
    build()
