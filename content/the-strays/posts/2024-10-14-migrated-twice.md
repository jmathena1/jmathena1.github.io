---
author: John Mathena
date: "2024-10-14"
title: Hugo is so nice, I migrated twice
---

After changing my blog and poetry site build systems to Hugo, I thought why not move everything to Hugo? 

I was recently updating my main website, which lives in its own repo. With my repos for blogging and poetry, 
that brings us to three repos with pretty much the same CSS, headers, footers, and all that jazz. 

I'm learning Go for a different side project so I figured why not go full in on Hugo. You don't need all that 
much Go knowledge to build a relatively simple site like mine in Hugo, but it doesn't hurt. And the nice thing 
about static site generators is that, well, they generate static files for your site. So if I get tired of Hugo, 
I can take my generated HTML files and go somewhere else. 

I definitely had to obtain a deeper understanding of Hugo templates to make this monorepo work compared to my 
other two Hugo sites, but I chunked the migration process pretty well so it didn't seem insurmountable. I started
with the main pages on my personal site:
- resume
- portfolio
- wiki
- blogs

### Resume
My resume was pretty easy. Once I figured out what formatting I need to to keep in the Sass file and what I could
accomplish in Markdown, it was pretty smooth sailing.

### Portfolio
The portfolio was a bit trickier because I realized I needed some way to apply the Sass across all the projects I
wanted to showcase. But the `range` function in Hugo templates ended up coming in handy.
```
...
<details id="collapsible-sections">
    <summary id="personal-projects" class="portfolio-header">
        <h3 id="header" class="portfolio-header">
            Academic Projects
        </h3>
    </summary>
    {{ range where .Site.RegularPages ".Params.portfolioType" "==" "academic" }}
        <div id="balto-city-salaries" class="portfolio-description">
            {{ .Content }}
            <a href={{ .Params.projectLink }} target="_blank" style="text-decoration:none;">
                <br>
                <button class="project-view-button">View Project</button>
                <br>
            </a>
            <br>
        </div>
        <br>
    {{ end }}
</details>
...
```
I maintained the `details` and `summary` html tags from my original site and added parameters to the content files.
That way I could `range` through different types of projects and display them together. `.Site.RegularPages`
specifies that you want to look at content files that match the directory of the layout file. So here, I'm looping
through all the content files in the `portfolio` content directory and displaying a link to that file if the `portfolioType` is `academic`. `details` and `summary` are super useful when you want to display different categories of 
content to users, but keep the interface clean and tidy.

### Wiki
I thought migrating my digital garden wiki would be easy, but I couldn't figure out how to distinguish between
what I call parent and child pages. Basically, I categorize my wiki topics and nest sub-topics within the main ones
that appear on the [home garden](/wiki-pages) page. I again turned to custom parameters on the content files, this
one is `wikiType`. I applied `range` to the wiki directory and only display wiki pages with a `wikiType` of 
`parent`.
```
...
{{ range where .RegularPages "Params.wikiType" "==" "parent" }}
    <div class="garden-section-header">
        <h4>
            <a href="{{ .Permalink }}">
                {{ .Title }}
            </a>
        </h4>
    </div>
    <br>
{{ end }}
...
```

### Blogs
Since I wrote the blogs using Hugo already, this one was pretty straightforward. I wrangled with the Sass for
awhile because I wrote the blogs as standalone sites and now they existed as part of a larger site with its own
header and everything.

I feel like I've re-architected these sites a million times, but I think that's the point! Who knows how long I'll
stick with Hugo, but I'm pretty satisfied with the end result.

