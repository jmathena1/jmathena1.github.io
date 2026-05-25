---
author: John Mathena
date: 2026-05-26
title: Some Links and Stuff (2026-05-26)
---

It's been awhile so I've got a bunch of fresh, new links plus some updates

1. [Fun blog posts](#fun-blogs)
2. [Live reload for local development](#live-reload)
3. [Changing jobs!](#new-job)

### Some fun blog posts from my favorite bloggers {#fun-blogs}

[https://www.drcathicks.com/post/on-craft](https://www.drcathicks.com/post/on-craft)

- [Dr. Cat Hicks](https://www.drcathicks.com/) is a psychologist who
  specializes in studying software teams and tech work. They have a podcast,
  this blog, and post frequently on Mastodon. Dr. Hicks spends this post
  talking about their Grandpa's love of his Craft for the craft's sake. It's so
  well written and touches on a lot; taking pride in your work, the importance
  of mentorship, avoiding gatekeeping in communities of practice. The talk
  dovetails really nicely with Vicki Boykis' ["Build Yourself
  Flowers"](https://vickiboykis.com/2026/04/20/build-yourself-flowers/) keynote
  at the annual Applied Machine Learning Conference in Charlottesville last
  month.

[https://piechowski.io/post/how-i-audit-a-legacy-rails-codebase/](https://piechowski.io/post/how-i-audit-a-legacy-rails-codebase/)

- Last year, another director at my former employer left and I suddenly found
  myself the owner of a Ruby on Rails monolith despite never having written any
  Ruby. This post has a good mix of practical advice on auditing the health of
  an existing Rails project using specific tools (and AI, responsibly!). But
  the author also walks through some questions you should ask the people around
  the project and puts that first! Great approach.

[https://blainsmith.com/essays/humanities-in-the-machine/](https://blainsmith.com/essays/humanities-in-the-machine/)

- Blain details brief histories of some giants in Computing and argues how
  most, if not all, these luminaries rigorously studied various domains and
  areas outside computing and other technical disciplines; be they Philosophy,
  Foreign Languages, Literature, etc. We programmers need to read and do things
  beyond the keyboard! Especially things that don't appear obviously applicable
  to tech. This is hard, but essential to being good developers but more
  importantly good people.

[https://evanhahn.com/all-tests-pass-a-short-story/](https://evanhahn.com/all-tests-pass-a-short-story/)

- Evan here tasked an AI with writing a small compression implentation in a
  language new to him called Arturo. Evan gave the bot a AGENTS.md file plus
  some Go test cases and let it loose. He beamed when the agent finished with
  all the tests passing, but then he realized the agent just wrote an Arturo
  shell to call Python. Sigh :( very funny though!

[https://belderbos.dev/blog/rust-made-me-a-better-python-developer/](https://belderbos.dev/blog/rust-made-me-a-better-python-developer/)

- Not sure if I'll ever learn Rust. I guess if someone every decides to make me
  a systems programmer or if I do one of my crazier projects on one of my
  neverending lists. I like the mindset here. I do have plans to learn basic C,
  not necessarily because I'm gonna be using it at work. Learning other
  approaches to working in your field naturally exposes you to new ways to
  think, new ways to solve problems. And I don't think we're going to run out
  of problems anytime soon.

### I added a live reload feature to mysite! {#live-reload}

Since I moved away from Hugo earlier this year, I lost my live reload feature.
So when I'm adding something to my site or writing my blog, I have to manually
run the `make build` command to refresh the files. Not a huge burden, honestly,
but I wanted to track a crack at setting this up myself.

Naturally, there are numerous approaches since we are using Python here. A
couple months ago I used one of the Copilot models with OpenCode to make me
some options for adding live reload to my local development server. One of the
options was FastAPI, which is a popular Python library I've never used so I
asked it to build me a first attempt. It...did not work.

After coming back to my branch after a couple months, the `dev_server.py` file
it made just seemed way too heavyweight to me. I went back to the drawing board
and came across the `livereload` package, which seemed a much better fit. After
hacking away at it and a couple other miscellaneous things for an hour or so, I
had a working live reload. The code below is the entire `dev_server.py` file.

```
import logging

from livereload import Server, shell

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    server = Server()

    server.watch("src/", shell('make build'))

    server.serve(port=8000, liveport=8001, root="public")
```

I could make it a little smarter if I really wanted to. It's very greedy and
watches everything in `src`. Right now, it just builds the entire site anytime
something changes. But since my site is small and takes about 2 or 3 seconds to
build, I'm not too worried about it. The changes won't be difficult if I ever
decide to make them (or have an LLM do it). Don't overengineer!

### New job! {#new-job}
My last day at 2U was May 22. I've got a little time before I start my next
gig, which I'm using to blog and make site enhancements as you can see! I've
been at 2U almost 4 years and it was first time programming with a team of
fellow programmers. I met and worked with incredible people who helped me
develop into a competent engineer (and manager)!

Over last 12 months, I went from being a first time manager of less than 10
people to managing nearly 30 across 3 different teams. I received a lot of
great feedback from my colleagues and higher-ups about my performance and the
experience helped me realize that I do like managing and supporting developers.
Ultimately, I decided to pursue other jobs because my remit continued to grow
and I felt I wanted to be more hands-on for the current stage of my career,
rather than a mile wide and an inch deep. While I'm sad to be saying goodbye to
some great people, I'm excited to work in a new org with new challenges.

If you've made it this far, thanks for reading!
