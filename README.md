# Evan Hahn optimizes his public transit purchases for July 2015

This project has no bearing on anyone's life other than my own, which is why I'm publishing it for the world to see.

I was going to spend part of the remaining month (20 more days) riding [Caltrain](http://www.caltrain.com/) and part of the month riding [Muni](https://www.sfmta.com/). I wanted to spend the smallest amount of money, but the amount varied depending on how many days I was riding each.

I wrote a little Python script (Python 2, not Python 3) script that figures out the optimal set of tickets/passes to buy. It works like this:

    $ python best.py

    0 days of Caltrain, 20 days of Muni
    Muni month pass for 70
    Total: 70.0

    ...

    7 days of Caltrain, 13 days of Muni
    1 8-ride tickets for 50.0
    3 Caltrain days 40.5
    13 invidual tickets for 58.5
    Total: 149.0

    ...

It's not wildly polished but it got the job done for me!
