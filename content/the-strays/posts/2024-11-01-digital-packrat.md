---
author: John Mathena
date: "2024-11-01"
title: On Digital Packrats and Why Open Source Rules
---

In my last post I talked about how exciting and relatively seamless my migration to Hugo was. Wellllll, it broke in
prod. NOOO! But I had an idea. I posted on the Hugo forums for help! I posted late on a Friday night; maybe around 
8pm or 8:30 (after checking the post it was just before 8pm) but after an hour or a little less, a very nice
person named Joe cloned my website repo and started debugging for me.

He commented that the hugo build process is indeed building all the expected files. He also recommended I start
using relative links throughout my site, which I obliged. We then started going back forth about the custom domain
I'm using for my site and how that was set up. 

The issue that caused me to post was that all my pages were loading except the `droppin-dimes` part of the site.
Those pages displayed 404 not found errors through GitHub Pages (where I host this site), which we found odd since
we confirmed our build process was in fact building all the necessary html files. Eventually, I told Joe that I
migrated `droppin-dimes` and `the-strays` from their own repos. 

Then he discovered that the original `droppin-dimes` repo was still deployed a page to 
johnwmathena.com/droppin-dimes, which is the address I attempted to use in my new monorepo. 
Joe summarized the issue in his last reply to the post, which I will quote below:

> That was a good learning experience.

> 1) If you create a GitHub repository for a personal GitHub Pages site…`https://github.com/user/user.github.io`  

> 2) And then configure that repository with a custom domain name…

> 3) And the published personal GitHub Pages site has a subdirectory named “foo”…

> 4) You will have a conflict if you have a repository named “foo”

> `https://github.com/user/foo`
>So, in your case, we could have renamed the droppin-dimes directory to dropping-dimes and it would have worked fine (no conflict).

I'll add the link to the post at the end for the record but there's two main takeaways here, at least for me. 1)
Don't be a digital packrat. Delete old stuff! If I would've just deleted my old repos once I moved all my old code,
this probably would not have happened. 2) Open source rules! Having all my code publically available allowed a
fellow programmer to not only see and poke at the issue in the initial codebase, but also check all my other work
to see if something in another code repository was mucking things up (which was the case here!). This would have
been a lot harder if I locked my code behind paywalls. 

[https://discourse.gohugo.io/t/personal-github-pages-site-with-custom-domain-conflicts-with-another-repo/52238/11](
https://discourse.gohugo.io/t/personal-github-pages-site-with-custom-domain-conflicts-with-another-repo/52238/11)
