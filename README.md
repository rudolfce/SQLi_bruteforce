# SQLi bruteforce for Natas15 with mechanize/Python #

Natas wargames can be found in http://overthewire.org/wargames/natas/
To clean my conscience, I censored the password. Come on, you can beat Natas14.

## To other players... ##

First of all, if you haven't found the answer by yourself, I'll give you one
more chance here: you can still turn around and keep playing the game. You are
the one who benefits from finding things by yourself. Copying my solution won't
teach you much.

## Brief discussion ##

This is one possible solution for the Natas15 wargame, at least the only one I
figured out. It could be made general purpose by tweaking stuff from files
and/or command line, but I didn't think it was worth such an effort. It could
also be made multithreaded, but the same rule applied here.

Not general purpose and not multithreaded, it is still one possible solution.

The page code allows to inject SQL code by closing a double bracket. It was
desidned to lookup the database and search if the typed user exists on the user
table. It becomes interesting when you notice (by trial) that this particular
user table has a "password" column. It also has the user Natas16, wich is the
one whose password we search.

However, the output from queries is not displayed, only one message that says if
the user exists or not. To say "User exists", it actualy only verifies that
there is an answer to the submitted query. With this in mind, one could try out
injecting some code and try to guess by trial and error the password for Natas16.
And that is when bruteforce comes in handy.

The passwords so far, even if we don't understand quite well how a HTTP login
works, have always been letters (both upper and lower cases) and numbers, so
those are most likely to be the legal characters for this password. Since MySQL
doesn't make a difference between lower and upper case when comparing VARCHARs,
the comparison must be made from a binarization of the data.

Knowing all of this, a script can be written to try each character with some
wildcards and find out wich ones give an existing user.

## Unnecessary disclaimer ##

I left the output for every character attempt because I liked it. It's not
elegant, but amuses me for some reason. Of course it could be made to look less
like "I watch too much Hollywood hacker movies", but it is kinda fun to watch.
I won't change that. Period.