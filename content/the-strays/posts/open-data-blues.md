---
author: John Mathena
date: "2025-02-17"
title: "Open Data Blues: My Fight to Measure City Worker Salaries and Game With My Friends"
---

Found myself once again wrestling with Open Baltimore Data to measure employee salaries. I consider this project a follow up to my more 
[exploratory](https://citysalaries.johnwmathena.com) analysis of city employee salaries. Fortunately there's been a data update and this time I'm only looking at FY2024 salaries so I
can compare them to MIT's [Living Wage Calculator](https://livingwage.mit.edu) for Baltimore City in 2024. Unfortunately, there's still no data dictionary I can find and I still
have questions! Their API rate throttling is also annoying and it's pretty much guesswork to create a URL that will filter data the way you want, but I digress. 
I'm also just downloading the data set directly from the Open Baltimore Data site since it's pretty small (approx. 17k rows).

I'll list the fields provided on the [city salaries](https://data.baltimorecity.gov/datasets/baltimore::baltimore-city-employee-salaries-3/about) to ground my beef.
1. `Name`: seems straightforward
2. `Job Title`: two for two
3. `AgencyID`: Agency could be a bit nebulous but I think I follow
4. `AgencyName`: Ok together with number three, makes sense
5. `HireDate`: great wonderful love it
6. `AnnualSalary`: is this gross? I'd assume so
7. `GrossPay`: wait hold on
8. `FiscalYear`: yup got that

Overall, pretty good. The rub is that the two fields I really need (the two salary fields), I'm not super clear on. And the actual data fuzzies the picture even more. I'll go into
the details a little more in the actual project once I get it done (stay tuned!). But, I saw records where `AnnualSalary` was 0 but `GrossPay` had a value and vice-versa. If a worker
receives no annual salary from an employer, why would they have any gross pay? (pay before taxes, health insuances, etc.) Conversely, if a worker received no gross pay in a fiscal
year, why would they have an annual salary?

Now, I believe the city is including part time, seasonal, and other non-full time works in this data set. That could explain some strange data points. For example, there are hundreds
election judges who received very little gross pay, but also have no annual salary because they are not full time city workers. I also see what appears to be coaches or
teachers for recreation center activities that work part-time or intermittently. Maybe there's also records on employees taking some kind of leave of absence?

Bottom line is: open data is great! But _some_ documentation would be appreciated. I see the Open
Baltimore site lists some pages with data governance, annual reports, and a blog. Perhaps somewhere in those pages, I'll find some answers.

Last month, I finally released a project I'd promised some of my friends for months: a Discord bot. [gamerGorlBot](https://github.com/jmathena/gamer-gorl-bot) allows to compare each
other's Steam wish lists and see what wishlisted games may be on sale. I stood up the bot pretty quickly with help from the Discord Developer documentation. I did find out after the 
fact that there are even easier libraries others have built to further streamline the bot building process (Discord.js and Discord.py are what I'm referencing). But no biggie, less
dependencies for meeee! But only slightly, it's still a Node/Express app. 

Anywho, I saw someone made a [Steam wish list calculator](https://github.com/The-HopelessGamer/steamwishlistcalculator), which I referenced to build queries to the Steam API. 
But otherwise, I resorted to the Steam API documentation, which you can find [here](https://steamcommunity.com/dev). From that link alone, I couldn't really figure out how to get
information about actual games. Through googling though, I managed to find [these docs](https://steamwebapi.azurewebsites.net/) aptly named "Better Steam Web API Documentation". I
would highly recommend anyone wanting to play with Steam data to use the better docs. God bless programmers putting things out there for free. 

The way I'm writing this up makes it seem like less of a pain than it was. I'm recounting my woes diving into documentation at least a month or so after the fact, so I'm missing some
of the deets. But it was a pain in the ass for sure. I'd also not done much user facing web development like that, so that was a learning curve. Aren't they all? I deployed the bot
on fly.io and let me tell you, if you have a small project definitely consider fly. Super easy and very cheap. Granted I've got like four users and only ever intend to have like
four users, but I remember putting one of my other side projects on GCP feeling so laborious. Good experience, but I'm in AWS land everyday. I'm whittling a stick, I don't need
a chainsaw, ya know?

I say all that to say...wait I forgot my closer. The throughline here is open data, open APIs, open whatever is great! We want more! But these products need a clear direction and
purpose. I did manage to find and skim a Data Governance Charter I found on the open data site, which is pretty good. There's a clear
[mission](https://docs.google.com/document/d/1fAAkhis1yaZVt3BsizjIhtghhLIrpGqcRQEcKWUW47g/edit?tab=t.0#heading=h.4dl6rd31mzg7) mentioned, which I love. Perusing the site more, I've 
found some surprising documents and information like some kind of Baltimore Data Academy? I wish they advertised this more. So good job, Baltimore! But do some more self-promotion.

Now for Valve, I'm not sure what building and maintaining a quality API really does for their business. I'm guessing that's why it's so meh. Moreover, I don't know what any of us can
really do about that except build our own stuff, which clearly several people did. Good for us! I think that's it. til next time
