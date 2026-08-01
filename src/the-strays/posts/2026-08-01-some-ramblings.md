---
author: John Mathena
date: 2026-08-01
title: Some Ramblings (2026-08-01)
---

I want to blog more, so I'm writing without as much focus as my other posts. Though as I wrote last sentence, I notice that I titled
three of my last five or so posts "Some Links and Stuff". We're ahead of the game baby!

Naturally, I'm reflecting on my first 2 months at a new job. Overall, very good! I've gotten a couple chores and bug fixes out and
am gearing up to add a more formal feature here in the next month. It's been great to be hands on keyboard again. I do miss some
of the mentorship and guidance you provide as a people manager. But since there's a senior in my title, I'm sure that opportunity
will present itself the longer I'm here.

I spent quite a bit of time trying to get one of our dockerized local development environments working as expected and updating
the documentation. Our DevOps lead is very nice and had gotten a lot set up already. Much of the work was adding test runners
and getting different projects to talk to each other over a docker network. Claude and Copilot helped a lot, I can't lie.
Although, I had to slow them down so I could review code and decisions. 

I'm new to Ruby on Rails in the backend and React on the frontend, which is the majority of the tech stack here. The LLMs are especially helpful when 
I know a Python-y or more general backend thing I wanna do, and just need help translating to Ruby and/or Rails. 
LLMs provide good debugging support and code review. Gemini has been kinda bad though. We still have Copilot in our repos but Gemini runs 
automatically, presumably because we are a Google Workspace shop and it's cheaper. I don't have a specific example off the top of my head, 
but I've seen other developers also comment on Gemini's suggestions "uh this isn't really accurate. here's why. going to ignore". People are diligent when
responding to comments though, so that's a plus.

I have to be really careful with React. I only knew the basics coming in, and I can't evaluate React code nearly as deeply as backend code of any sort. Our
frontend developers and product designers launched a component library for the whole company and devs are supposed to migrate legacy components to the new
library when they come across old code. I asked the LLMs to migrate a pretty complex Form and hardly understood any of the output. So, I just held off
on the migration and made a ticket to go back in and complete it when I could go through it deeper. It wasn't mission critical, and other devs said
this was totally cool, but I can imagine getting pressured to just chug that along under different circumstances.

I still haven't quite figured out how to marry using these LLMs for coding while continuing to hone and grow my own skills. I know people out there have ideas
and strategies. I just write stuff by hand as consistently as I can and use these tools only when I can validate the output well and feel confident I can do
the work myself. I'm not sure if that's the best approach, but that's the tune I'm singing for the time being.

Again, these robots are helpful. But man, the externalities are ROUGH. People seem to argue about the magnitude of different problems with this era of "AI" tools;
environmental impact, legality of training data use and acquisition, programming skill atrophy, etc. However, it seems clear all these problems are real. I love
that the local models and tools are getting good. Vicki Boykis wrote a [post](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) about
that. I'm working on setting up a NAS and I could set up and old laptop I have lying around to work with the NAS and run some thing locally. Then I'd feel better
about leveraging a helpful tool and not giving money to the richest and most ethically questionable people on earth right now. 

Other than all the externality stuff I mentioned above (which should be enough for anyone to question if we should even use these things at all, 
for what it's worth), I really wish more places were using LLMs for one of the things they are best at: search and summary! I mean, I'm sure people are, but, ok
let me break it down. So every place I've ever worked has had some collection of internal knowledge documents for everything from strategy, operations, HR, you
name it. And the workers at most of those places usually agree that no one can find a goddamn thing. It's all a mix of Google Drive / One Drive documents with
Confluence and SharePoint mixed up in there plus Slack and Teams doing their best to hold things together. 

Now if things were organized, this would be a TREMENDOUS
opportunity for an LLM to provide anybody with a way to talk with your organzation's knowledge base. Atlassian, Microsoft, etc., do have AI features for the
docs you shove on their platforms, but in many places it's likely garbage in garbage out as they say. I don't understand why every sufficiently large company
doesn't go hire a librarian or a knowledge management expert (this is a real field, I promise! someone I went to school with does this! s/o Sarah) and have them
make their company knowledge base not suck. I mean I can guess the reasons but it's so obviously a win across the board. This would also help people learn and
upskill and would prevent turnover from killing a company's institutional knowledge. The improved learning and upskilling from having company knowledge and history
easily accessible for newer employees could also lower turnover itself.

**Better knowledge base = everybody knows more = everybody can do better = the organization does better**

Well that's work. Personally, I've been travelling quite a bit. I've been to the beach twice; once to Rehobeth Beach in Delaware with friends and once to Hutchinson
Island near Fort Piece in Florida with my wife and my in-laws. Definitely recommend going to the beach. Florida is very hot in July, though this is likely not
surprising. I feel extremely fortunate and lucky to be able to travel and enjoy time off with family and friends, one because it rocks and it makes life
worth living, and two because of how bonkers the world around us can be. It becomes that much more important to take time to have fun.
