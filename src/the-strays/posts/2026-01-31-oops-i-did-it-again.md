---
author: John Mathena
date: 2026-01-31
title: Oops, I did it again! Another new site build strategy
---

I ditched Hugo after almost 2 years. I came across a post detailing a vanilla HTML/CSS approach.
It also leveraged uv to run a build script that converted the markdown files to HTML. I modified said script and
added a step for my static site search engine I run on my wiki pages. This drastically simplified my build process.
Though as of writing, I have yet to rewrite my GH action for deploy, so maybe I shouldn't speak so soon. See below
for the post I used as insipiration for this refactor.

[https://www.vijayp.dev/blog/rewrite-plain-html/](https://www.vijayp.dev/blog/rewrite-plain-html/)

## Creating a `src` directory and tidying up

I created a copy of my hugo generated `public` directory and used it as reference for both the templates I applied to my
markdown files and the generated HTML files resulting from my build script. After creating a `src` directory and an `index.html`
file, I moved my assets and made sure my home page rendered as expected. Then I needed to focus on the other main pages on my
site that are in my navigation bar my resume, my portfolio, and my wiki/digital garden (though I actually did a lot of this last).


