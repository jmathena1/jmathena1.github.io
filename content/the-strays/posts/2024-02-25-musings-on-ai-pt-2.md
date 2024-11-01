---
author: John Mathena
date: "2024-02-25T00:00:00Z"
title: Musings on AI pt 2
---

Though I don't feel anything from pt 1 was incorrect, I wanted lend a bit more credulity to AI and Machine Learning work. I'm gonna reference mostly work and posts from
a machine learning engineer and tech writer I follow, Vicki Boykis. She has a great post from Feb 2023 on Chat GPT titled 
["What should you use Chat GPT for?"](https://vickiboykis.com/2023/02/26/what-should-you-use-chatgpt-for). Part of her assessment from then:
> "So, for myself, my rules for engaging with Chat GPT are to give it small, inconsequential things it can iterate well on and that I have the ability to check..."

I think I saw Kareem Carr say something similar on Twitter (also a great follow if you're not already).  

Seems a good assessment. And this coming from someone with a lot of experience with software as a whole and machine learning in particular. Now I've also seen some
(mostly on Twitter though again) compare the advent of LLM based coding tools to compilers. That doesn't quite sit right with me. I don't have a CS degree nor have I
event taken a CS class, but I've been programming for the better part of a decade (professionally for about five years) and I can read so I'm gonna try to break down
why. Maybe I'll look back on this series in 10 years and cringe but whatever at least I tried.

Compilers essentially translate code written in one language into another language. This allows us to write in more human readable (high level) languages like Java rather than
machine code (literal ones and zeroes corresponding to circuits and gates on the hardware). 

Since computer scientists built the first compilers in the mid 20th century, we've gotten better and better at allowing software developers to write programs quickly and without caring so much the hardware. Whether this is good or bad depends on who you ask. I think lower
barriers to pushing an app out the door has definitely led to some bloated software. When programmers don't have to care about optmizing how their programs use hardware resources,
they won't. This is something I'm trying to care more about as I grow as a developer and programmer.

Enter AI that can write apps. When you can literally just type "build me a to do list app" and know next to nothing about programming or software development, and have ChatGPT give
you something that may actually run, that's not really programming. When you open a program written in Python and it gets compiled into bytecode and interpreted into machine code, you are utilizing
explicit processes written by another human. When you open a program you got from ChatGPT, you're getting a best guess. ChatGPT is troving the mountains of data on existing computer code
it's seen and trying to throw something back at you that seems to match what you said. 

It's very cool and can be accurate! But this is not what happens when you write computer code. Computers, for better or worse, do exactly what you tell them. You ask a computer to "Print"
instead of "print", not gonna run. You say a variable is equal to "one" instead of 1 (depending on the language), doesn't know what you're talking about. I'm sure every programmer will wax poetic about times like
these. But what computers lack in forgiveness, they make up for in precision (usually).

I could go on, but yeah these AI tools are different than compilers. I'm not trying to gatekeep software and programming by any means. And I also know that creating efficient, quality
software quickly is a real value-add and something worth pursuing. But I think you need trained professionals to do that. These AI code assistant tools could help programmers
reference unfamiliar languages and frameworks faster and maybe do some auto-completion (though these kinds of features are not new to programmers). 

There's certainly room for improvement in modern software development, but I'm not convinced unleashing the AI tools will fix the current problems in the field. 
I'm worried they'll make things worse.
