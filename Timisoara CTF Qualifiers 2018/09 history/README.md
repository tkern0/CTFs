### History
30 points
> Hey buddy, today at our history lesson a guy from some sort of consortium came to speak about some standard... it was soooo boring, that at some time I fell asleep, but I used my audio recorder program to take some notes about his speech. Unfortunately there's a sentence missing (a bug?). Can you help?

---

We are given `history`, a linux executable. Running it prints the following text:

```
==========================================
Ground work began in late 1987 with initial discussions
between three software engineers -- Joe Becker of Xerox Corporation
Lee Collins who was then with Xerox, and Mark Davis, then of Apple Corporation.

Peter Fenwick visited Xerox PARC, joined by Nakajima from Toronto, and
Alan Tucker and Karen-Smith Yoshimura of the Research Libraries Group, Inc.
The discussion led to the architecture of what later becomes known as ☐ “begin at 0 and add the next character.”

First prototypes begin at Aṗṗle.

In the fall of 1988, Collins began building a database
of characters.
==========================================
```

What it seems like you're meant to do is work out some way to print the sentence that has been replaced with "☐", which should then contain the flag. However, I had a bit of a different approach. I opened it in a hex editor, scrolled down a bit, and just found the flag sitting there:

![timctf{unic0d3\_1s\_mr\_w0rldw1d3}][00_flag]


[00_flag]: ../images/09_00_flag.png
