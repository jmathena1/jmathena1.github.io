---
author: John Mathena
date: "2024-03-16"
title: Same Blog, Different Build. On to Hugo!
---

I migrated my blog to [Hugo](https://gohugo.io/)! I've been using [Jekyll](https://jekyllrb.com/) to build
my blogging site for the past couple years but I read that it is no longer actively supported. Several bloggers
I follow have made the switch to Hugo and claim the build speed is a lot faster. Though that's not really a concern
for me at the moment, if I keep publishing here I'll eventually run into those problems.

The biggest hurdle was figuring out how Hugo does templating differently than Jekyll. Once I figured
that out, it was pretty smooth sailing. Hugo actually has a specific Jekyll import function you can use.
	
> `hugo import jekyll <path-to-old-blog> <path-to-new-blog>`

That brought over all four of my posts and my assets I think. I'll post the links I found essential to getting set
up.

1. [Hugo Quickstart page](https://gohugo.io/getting-started/quick-start/)
> - Gets you a first post and basic configurations to see your site run in browser locally

2. [Hugo template lookup order reference](https://gohugo.io/templates/lookup-order/)
> - Shows you how Hugo looks through your directory for templates depending on the type of page you're creating

3. [cloudcannon Hugo tutorial](https://cloudcannon.com/tutorials/hugo-beginner-tutorial/)
> - one of the first results when I googled for tutorials. I found it helpful for organizing my templates.
My site is a bit simpler but helped illustrate how to use the template lookup order and create some good templates.

4. [Chen Hui Jing's Jekyll to Hugo Migration post](https://chenhuijing.com/blog/migrating-from-jekyll-to-hugo/)
> - Didn't read the whole thing but was very in depth and would probably be best for those migrating large blogs
to Hugo.

If you read through all that, you'll be in good shape to migrate a blog or set up your own honestly. 
Happy blogging!
