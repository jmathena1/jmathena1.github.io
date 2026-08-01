import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, time as dtime, timezone
from pathlib import Path

import pandoc
from feedgen.feed import FeedGenerator
from frontmatter import Frontmatter


OUTPUT_DIRECTORY = Path(os.getenv("BUILD_DIR", "public"))
SITE_URL = "https://www.johnwmathena.com"
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


def render_markdown(body: str) -> str:
    doc = pandoc.read(source=body, format="markdown")
    return pandoc.write(doc, format="html")


def read_template(path: str | Path) -> str:
    return Path(path).read_text()


def write_html(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)


def build_wiki(
    content_title: str, content_description: str, posts_directory_name: str
) -> None:
    post_template = read_template("src/templates/wiki-template.html")

    posts_directory_path = Path("src/wiki-pages")
    post_titles = []
    post_html_snippets = []
    for markdown_path in posts_directory_path.glob("*.md"):
        slug = markdown_path.stem

        post = Frontmatter.read_file(markdown_path)
        title = post["attributes"]["title"]
        wiki_type = post["attributes"].get("wikiType", None)

        # Only include "parent" wiki pages in the index.
        if wiki_type == "parent":
            post_titles.append(title)
            # Generate the HTML snippet for this post's link on the index.
            post_html_snippets.append(WIKI_POST_SNIPPET.format(slug=slug, title=title))

        post_html = post_template.format(
            title=title,
            content=render_markdown(post["body"]),
        )
        write_html(
            OUTPUT_DIRECTORY / posts_directory_name / slug / "index.html", post_html
        )

    sorted_pairs = sorted(
        zip(post_titles, post_html_snippets, strict=True), key=lambda pair: pair[0]
    )
    sorted_snippets = [pair[1] for pair in sorted_pairs]

    index_template = read_template("src/wiki-index.html")
    index_html = index_template.format(
        content_title=content_title,
        content_description=content_description,
        posts="\n".join(sorted_snippets),
    )
    write_html(OUTPUT_DIRECTORY / posts_directory_name / "index.html", index_html)


def build_content_site(
    content_title: str, content_description: str, posts_directory_name: str
) -> None:
    post_template = read_template("src/templates/post-template.html")

    posts_directory_path = Path(f"src/{posts_directory_name}/posts")
    post_dates = []
    post_html_snippets = []
    posts = []
    for markdown_path in posts_directory_path.glob("*.md"):
        slug = markdown_path.stem

        post = Frontmatter.read_file(markdown_path)
        title = post["attributes"]["title"]
        date = post["attributes"]["date"]
        author = post["attributes"]["author"]
        formatted_date = date.strftime("%B %d, %Y")
        content_html = render_markdown(post["body"])

        post_html = post_template.format(
            title=title,
            date=formatted_date,
            posts_directory_name=posts_directory_name,
            content_title=content_title,
            content=content_html,
        )
        write_html(
            OUTPUT_DIRECTORY / posts_directory_name / slug / "index.html", post_html
        )

        post_html_snippets.append(
            POST_SNIPPET.format(
                posts_directory_name=posts_directory_name,
                slug=slug,
                title=title,
                date=formatted_date,
            ),
        )
        post_dates.append(date)

        # Collect the record used to build the Atom feed.
        posts.append(
            {
                "slug": slug,
                "title": title,
                "date": date,
                "author": author,
                "content": content_html,
            }
        )

    sorted_pairs = sorted(
        zip(post_dates, post_html_snippets, strict=True), reverse=True
    )
    sorted_snippets = [pair[1] for pair in sorted_pairs]

    index_template = read_template("src/blog-index.html")
    index_html = index_template.format(
        content_title=content_title,
        content_description=content_description,
        posts_directory_name=posts_directory_name,
        posts="\n".join(sorted_snippets),
    )
    write_html(OUTPUT_DIRECTORY / posts_directory_name / "index.html", index_html)

    build_feed(
        content_title=content_title,
        content_description=content_description,
        posts_directory_name=posts_directory_name,
        posts=posts,
    )


def build_feed(
    content_title: str,
    content_description: str,
    posts_directory_name: str,
    posts: list[dict],
) -> None:
    section_url = f"{SITE_URL}/{posts_directory_name}/"
    feed_url = f"{section_url}atom.xml"

    fg = FeedGenerator()
    fg.id(section_url)
    fg.title(content_title)
    fg.subtitle(content_description)
    fg.language("en-US")
    fg.link(href=section_url, rel="alternate")
    fg.link(href=feed_url, rel="self")

    # Add entries newest-first so readers show the latest post at the top.
    newest = None
    for post in sorted(posts, key=lambda p: p["date"], reverse=True):
        post_url = f"{section_url}{post['slug']}/"
        published = datetime.combine(post["date"], dtime.min, tzinfo=timezone.utc)
        if newest is None:
            newest = published

        fe = fg.add_entry(order="append")
        fe.id(post_url)
        fe.title(post["title"])
        fe.link(href=post_url, rel="alternate")
        fe.author({"name": post["author"]})
        fe.published(published)
        fe.updated(published)
        fe.content(post["content"], type="html")

    # The feed's own timestamp reflects the most recent post.
    if newest is not None:
        fg.updated(newest)

    feed_path = OUTPUT_DIRECTORY / posts_directory_name / "atom.xml"
    feed_path.parent.mkdir(parents=True, exist_ok=True)
    fg.atom_file(str(feed_path))


def run_pagefind() -> None:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pagefind",
            "--site",
            str(OUTPUT_DIRECTORY),
            "--output-path",
            str(OUTPUT_DIRECTORY / "pagefind"),
            "--exclude-selectors",
            "body:not(.wiki-page)",
        ],
        check=True,
    )


def build() -> None:
    start = time.perf_counter()

    # This script writes output to the public/ directory. If it exists, delete it.
    if OUTPUT_DIRECTORY.exists():
        shutil.rmtree(OUTPUT_DIRECTORY)

    shutil.copytree("src/static/", OUTPUT_DIRECTORY)

    build_content_site(
        content_title="The Strays",
        content_description="The home of John Mathena's stray thoughts",
        posts_directory_name="the-strays",
    )
    build_content_site(
        content_title="Droppin Dimes",
        content_description="ludirous lyrical mastery",
        posts_directory_name="droppin-dimes",
    )
    build_wiki(
        content_title="John's Digital Garden",
        content_description="The place where I store the stuff my brain swears I'll come back to later",
        posts_directory_name="wiki-pages",
    )

    run_pagefind()

    elapsed = time.perf_counter() - start
    print(f"Site build complete! ({elapsed:.2f} seconds)")


if __name__ == "__main__":
    build()
