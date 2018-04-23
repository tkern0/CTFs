### Substitute Teacher
100 points
> The teacher did not make it to class today however he sent somebody to teach you about permutations and stuff.
>
> NOTE: Once you got the flag you need to add {}

---

We get given `ciphertext.txt`, a 800kb text document encrypted with some unknown cipher. The first thing I tried was just searching for "timctf" or the curly brackets, but nope, that'd be too easy. Then looking through it a bit I noticed that there were quite a few blobs of plaintext in all caps. The one in particular that caught my eye was the following:

```
THE AMERICAN UNIVERSITY OF PARIS
zgedxtr zgbsbncs
AN EVENING WITH ROBERT LANGDON
PROFESSOR OF RELIGIOUS SYMBOLOGY,
HARVARD UNIVERSITY
```

Googling this I found out Robert Langdon is a character in The Da Vinic Code. So I find an excerpt near the beginning and what do you know - it seems to match up. It seems like the entire text was just run through the same script used for Back in Time, all capital letters, numbers, and symbols all stay in the same place while lowercase letters have been shuffled. So using the small excerpt I was able to fully reconstruct the key. I wrote a small script to reverse it, and then I could just search for "timctf" and find it.

![timctf fr3quencyan4lyS1s1sc0ol][00_flag]

The flag makes it seem like I was supposed to do frequency analysis, but I think my way is much easier.


[00_flag]: ../images/08_00_flag.png
