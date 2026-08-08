---
author: John Mathena
date: 2026-08-07
title: How to be helpful and How (not?) to run robots locally
---

This past week I wrestled quite a bit with React and Tailwind trying to update the design of some question
and radio input button pairs in our app. I made it about 95 percent of the way there and then I paired with one
of our senior frontend engineers to do the rest. They drove and we walked through the offending components together.

I correctly added some flex containers to the question and answer components so they would be vertically centered
with each other. However, I neglected a breakpoint and `flex wrap` option that would allow the radio input answers
and their labels to slide underneath the questions if the user entered data on mobile. Instead the fairly short
questions just squished up against each other as the three radio buttons took up more and more of the viewport.
My apologies that I do not have a visual. I suppose I could create a CodePen or something to illustrate the point,
but I'm a bit too lazy right now. ¯\\_(ツ)_/¯

Our senior FE engineer also gave me some helpful devtool tips for looking into CSS elements and testing changes.
They even manually increased and decreased the browser window to make sure the breakpoint occurred at the same width
for all the questions. I both learned a lot and got a very thorough commit to cap off my PR after this session.

Today, I've been trying to get some local models up and running to use with OpenCode. I had Ollama installed inside
WSL on my gaming PC from some experimentation last year. I wanted to grab some of the newer models that could make
tool calls, but I had to be selective since I'm limited by my hardware.
- NVIDIA GeFOrce RTX 3060 with 12 GB of VRAM
- 16 GB of RAM on the system
I've got a two month old Macbook Pro with a crap ton of processing power for work, so I lowered my expectations a bit.
Not too much though after reading about how much better local models had gotten. 

I downloaded some Gemma 4 models first; 12 billion and 26 billion parameter versions I believe. Though, I think they
were a bit too big to run on my PC. So I pulled down some Qwen models as well, starting with 2.5-coder. I got OpenCode
and Ollama all configured, fired the thing up in my repo and it just kept printing out the CLI tools it *would* call
to answer my prompt rather than actually doing work, even in Build mode. 

I eventually figured out this was because Qwen2.5-coder's tool call formats don't always play nice with what OpenCode
expects. Very interesting and very frustrating! I ended up trying LMStudio as well just to see if Ollama was the 
problem. I got LMStudio working with Qwen3.5, and then switched back to Ollama to give it one last go. e Voila!
It works! It'll call git and grep and stuff like that. Cool!

I actually was chatting with Kagi Assitant throughout this to see if a robot could help me fix another robot. Kagi
told me to just run the commands the broken agent spat out and then paste the output back as the next prompt. That
would work, but, it kind of defeats the purpose right? It felt very cyclical and in a bad way. I managed to configure
the local LLM well enough to do some stuff, but it definitely can't go full YOLO mode (or even partial YOLO mode, 
to be frank) and that's probably not a bad thing.

I came back the next day and just started working through the codebase I hadn't touched in awhile the old fashioned
way. And I felt a lot better and learned a lot more. It became clear the command handler pattern I wanted to implement
and the types I needed to build and fix. I made a lot more actual progress towards my goal of refactoring and
rearchitecting than when I wrestled with Ollama and OpenCode for half a day.

Good reminder that old reliable methods are, well, old and reliable; pairing with a nice, patient coworker and
click-clacking your way through a codebase.
