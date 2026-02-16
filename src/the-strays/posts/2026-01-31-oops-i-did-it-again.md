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

### Creating a `src` directory and tidying up

I created a copy of my hugo generated `public` directory and used it as reference for both the templates I applied to my
markdown files and the generated HTML files resulting from my build script. After creating a `src` directory and an `index.html`
file, I moved my assets and made sure my home page rendered as expected. Then I needed to focus on the other main pages on my
site that are in my navigation bar my resume, my portfolio, and my wiki/digital garden (though I actually did a lot of this last).

### Refactoring `build.py` script for my site

I didn't have to change too much. I write a traditional blog, poetry page, and a wiki / digital garden. The blog and poems
use the same page layout and almost the same CSS. So I made the build script Vijay provided reusable for both sites' content.
I created a separate build function for the wiki pages, since they're quite different. Overall, still a very short script, topping
out around 159 lines or so.

### Web components for header and footer
I didn't have Hugo to make partials anymore, so I decided to use some JS to write web components for my header and footer.
This does mean that my `head.html` is a bit redundant on each page, but since I'm using html templates and Pandoc to generate so
many when I run `make build`, it works fine.

### Rebuilding my wiki search
I tried fiddling with `lunar.js` and got pretty far along. I generated the index, just needed to build the actual search box and then
I guess the build steps on deploy. But I realized I could just use PageFind like I had been with Hugo, so I went with that. PageFind
has worked fine for me and it's more batteries included. I could probably do some work on the search results. I think it is a little
too fuzzy right now, but that's a problem for another day.

Now I just gotta deploy the dang thing! I'll come back here if I have any problems I guess. Fingers crossed!

### UPDATE post deploy

This literally built successfully on the first run! Hooray!
