### SSS - Part 2
250 points
> This time the secret is split into even more parts using our very own implementation of the algorithm. I made sure to get rid of most of the shares too. There's no way any student can crack this one.

---

We get given three files, `shares.txt` a list of SSS keys, and `split.py` and `sss.py`, the scripts that made them. `sss.py` is a proper class to encode stuff using SSS, and as far as I can tell it doesn't really have a weakness. `split.py` however...

This challenge has the same basis as it's other part, we need to find a polynomial containing all the points, and then find it's value when x=0. To change it up however, they split the string into 4 parts encoded separately, they're now using a 12th order polynomial, and they only give us 10 points. This would normally make it impossible to reconstruct, but the critical error is that they don't generate new coefficients for each part of the string. Because the secret is encoded in the constants of each polynomial, if you were to plot them all you'd end up with the same line, just shifted up or down, 4 times. This also means it's really easy to find our missing points again, we just need to work out the offset between the different lines.

Working out the missing points was relatively easy, there were a few simple bugs but my first idea ended up working perfectly fine. The problem was then reconstructing the polynomials. I tried using pre made methods like numpy.polyfit() or scipy.interpolate.lagrange() but they didn't have the precision needed, only the first few bytes ever got values, and they were usually useless ones. I tried reading the wikipedia page on lagrange polynomial interpolation and implementing that myself, but like with Those Are Rookie Numbers I didn't quite understand the page. I then tried matrix operations, but again only got a few bytes and mostly useless ones. In desperation I tried manually working it out knowing the offsets and that the first string would start with "timctf{", and, while looking back on it I actually got kind of close, it didn't really lead anywhere. Finally I found someone else's script made for this exact purpose, decrypting strings from SSS keys for a ctf, plugged my values in there and got the flag.

```
t@t:~$ python py2_solver.py
timctf{d0_NOt_R3inV3nT_CrYpt0_Pl34sE}
```
