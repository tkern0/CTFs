### Porcupiney
50 points
> Do you feel safe?
>
> http://porcupiney.woodlandhighschool.xyz/

---

Loading up this site looks a lot like the last one. Luckily it doesn't have that annoying script running so I could click around a bit but again there's nothing hidden. It took me quite a few visits to find, but eventually I noticed that this was the only site in the ctf using https. Checking the certificate properties we can find something interesting.

![DNS NAME=nonononono.woodlandhighschool.xyz][00_Certificate]

Going to https://nonononono.woodlandhighschool.xyz and scrolling to the bottom gives us our flag.

![timctf{w00dl4nd_cr1tt3rs_s3cur3_chr1stm4s}][01_Flag]


[00_Certificate]: ../images/10_00_certificate.png
[01_Flag]: ../images/10_01_flag.png
