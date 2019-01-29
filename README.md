# Bot Ross
### a comment reply bot built in Python


This is a simple bot built to reply to any comment that mentions "happy little" with a random Bob Ross quote.


The Bob Ross quote is pulled randomly from an array embedded within the script.


The script then remembers which comments it has replied to so it doesn't double-reply, and also doesn't reply to itself.


However, it is not connected to any kind of persistent database, meaning the script cannot be interrupted and restarted, or else it risks re-commenting on previously commented posts.


It is not currently live, but meant to simply be a demo script.