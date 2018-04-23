### Secret Data
50 points
> One of the teachers is up to no good. We suspect he is planning to send data about the students to a secret organisation. Don't let him do that!

---

We get given `secret_data.pcapng`. One quick google later and I find out this is a wireshark capture file, so I install it and load up the file. The file has a total of 35048 captured packets, which seem to be pretty normal data from my extremely inexperienced point of view. So let's try a filter, let's just search for "timctf" anywhere in the data. Well turns out I'm in luck:

![timctf{wir3\_sh4rk\_is\_aw3som3}][00_flag]


[00_flag]: ../images/05_00_flag.png
