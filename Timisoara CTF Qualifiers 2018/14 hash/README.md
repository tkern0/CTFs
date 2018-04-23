### Hush Hush
150 points
> Can I get a hash collision?
> 
> nc 89.38.210.129 6665

---

We get given an ip and `hash.py`, the script running on that server. When you connect to the server the following happens:

```
t@t:~$ nc 89.38.210.129 6665
Hello stranger!
Nobody can break my hash but you are free to try.
First input: test
Second input: test2
Told ya!
t@t:~$
```

Looking at the script, to hash your input it appends the string "piper", turns it into an int, does a bunch of maths to it and then throws it into an md5 hash. My first though was to try send an empty string and a null byte, adding 0x00 to the front of the string won't change the int value but will change the string. Well turns out that worked perfectly fine first try.

```
t@t:~/$ python solver.py
Hello stranger!

Nobody can break my hash but you are free to try.
First input: Second input: Thix will never be printed anyway, timctf{d0UbT_3verYTH1nG}

t@t:~/$
```
