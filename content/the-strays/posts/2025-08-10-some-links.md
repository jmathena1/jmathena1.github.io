---
author: John Mathena
date: "2025-08-10"
title: Some Links and Stuff (2025-08-10)
---

So I've got lots of links and lots of stuff, I hope you're ready. I'm gonna try to make
a little table of contents to quickly hop through everything.

1. [Marimo rocks](#marimo)
2. [Some gripes](#some-gripes)
3. [Real Nerd Stuff](#nerd-stuff) 

### Marimo rocks and you should try it {#marimo}
I managed to crank out another Baltimore data project: this one looks at who owns the
vacant houses in the city. I chose Jupyter notebooks for an exploratory analysis of 
city employee salary data a couple years ago, and felt pretty meh about them. 
- Version control would work but the diffs were pretty hard to read
- I had trouble reproducing other peoples' Jupyter notebooks in the past
- They weren't very fast
- The editor kept breaking on me
I won't belabor the point, but I heard about Marimo on the Real Python podcast (I think?it may have been Changelog). I decided to give it a go.

First off, I installed it with uv (which I am still loving!) and added any dependencies
to my `pyproject.toml` file with a quick `uv add`. I really only needed like `numpy` and`duckdb` or some such. The command line tool made it easy to open tutorials, new notebooks, and more.

Marimo is written in Python, so the diffs are easy to read and version control is more
straightforward.

You can also read data straight from CSVs into Polars/Pandas dataframes or run SQL using
DuckDB. The SQL cell expose the results as dataframes that can be shared across the
notebook. However, Marimo is clever! I accidentally named a variable in a one cell the
same as a dataframe output from a SQL query in another cell. Marimo threw an error!
I was being careless and it stopped me! 

I ran into some issues on deploy, but I caused them myself for the most part by
including the data sources as CSVs with my notebook files. I needed to peruse the
documentation a bit to learn how to path my data sources correctly so I could read
them into the notebook both in my local environment and on my deployed site. I chose
to use their web assembly export feature. [Here are some docs](https://docs.marimo.io/guides/wasm/#including-data) about including paths to data sources so hopefully
my dear readers are spared some pain.

I'd highly recommend checking this out if you're on the market for a new
data analysis framework and you're a Pythonista.

### Some gripes but also some wisdom {#some-gripes}
I've seen many write about their exhaustion with the current GenAI bubble. I definitely
share the lack of enthusiasm, and the link below leads to yet another causualty in
the war on using your brain: training and mentoring. I certainly don't want to live in
a world where GenAI bots are left to train the "developers of the future", so what are
we to do? This one is long, but it's well worth the read. The second one is me all
day every day working in Elon Musk and Sam Altman's tech industry. I don't think Tech
was every the wonderful, meriotocratic field people made it out to be, but it sure
ain't now.
- [https://xeiaso.net/blog/2025/rolling-ladder-behind-us/](https://xeiaso.net/blog/2025/rolling-ladder-behind-us/)
- [https://paddy.carvers.com/posts/2025/07/ai/](https://paddy.carvers.com/posts/2025/07/ai/)

Reading about poverty is no fun, but articles like the one below I find very valuable
because they treat poverty like the very solvable issue that it is. The People's Policy
Project has been doing great writing, analysis, and research on US Social Policy and
the welfare state for years now. I'd also recommend Dr. Kathryn Edwards (@keds_economist) on most socials and her podcast, the Optimist Economy for more good economic policy
talk and analysis.
- [https://www.peoplespolicyproject.org/2019/09/16/the-us-welfare-state-cut-poverty-by-two-thirds-in-2018/](https://www.peoplespolicyproject.org/2019/09/16/the-us-welfare-state-cut-poverty-by-two-thirds-in-2018/)

A UCLA professor wrote this advice for assisting people learning to use computers nearly30 years ago, but I'll be damned if every piece on that page doesn't hold true. Quick
and well worth your time!
- [https://pages.gseis.ucla.edu/faculty/agre/how-to-help.html](https://pages.gseis.ucla.edu/faculty/agre/how-to-help.html)

### Real nerd stuff and things I want to try {#nerd-stuff}
I've been watching a lot of Kevin Powell's videos to clean up the CSS on my site. The
one below was the best explainer I've seen on building a sticky footer for your site.
I.e. a footer that goes to the bottom of your broswers viewport even if you don't have
content that extends that far. Kevin provides a couple options depending on if you
want to use flexbox, grid, or something else I think.
- [https://www.youtube.com/watch?v=yc2olxLgKLk](https://www.youtube.com/watch?v=yc2olxLgKLk)

I elected to go with the flexbox solution for my sticky footer, but the `<hr>` dividers
I used in my HTML resume disappeared. I went a googlin' and shockingly found myself 
at the doorstep of Stack Overflow once again. I got not only a solution but a very cool
explanation, with links and everything! I love programmers. Thanks for all the help
over this years, Stack. I hope the LLMs take a bit longer to do you in.
- [https://stackoverflow.com/questions/34365271/hr-inside-container-with-display-flex-become-corrupted](https://stackoverflow.com/questions/34365271/hr-inside-container-with-display-flex-become-corrupted)

I came across a really cool little independent research lab. One of the cofounders (at least I believe they are a cofounder) is none other than Martin Kleppmann of Designing
Data Intensive Applications fame. Name of the lab is Ink & Switch. They wrote a conference paper on local-first software. They discuss use cases, the limits of cloud-based
dominance we see now, and even walk us through a set of distributed systems algorithms
called CRDTs that they think could help power these new local first softwares. The
paper is pretty technical, but concrete and well-written.
- [https://www.inkandswitch.com/essay/local-first/#towards-a-better-future](https://www.inkandswitch.com/essay/local-first/#towards-a-better-future)

I feel like I come across a ton of wacky, classic hacker-type stories where a coder
just decided to poke at something to see if they could. These stories really keep
the original hacker ethos alive. The one below tells a tale of a house full of nerds
deciding to hack their WiFi-enabled washing machine.
- [https://nexy.blog/2025/07/27/how-i-hacked-my-washing-machine/](https://nexy.blog/2025/07/27/how-i-hacked-my-washing-machine/)



