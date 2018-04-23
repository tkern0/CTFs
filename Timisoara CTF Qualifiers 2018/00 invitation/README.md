### Invitation
120 points
> Yes! Our school is invited to a cool competition... now we need to prepare and work hard to be among the best! Let's do it!

---

We get given a PDF file, `invitation.pdf`.  When I opened it an interesting warning popped up:

!['This PDF Document might not be displayed correctly'][00_Display]

Because of this I just decided to open it up in notepad to see if there's anything special inside. Luckily it turns out PDFs are just plaintext so I didn't need to get a special editor. Right at the beginning I find something interesting - apparently PDFs support javascript.

![Javascript Excerpt][01_Javascript]  
[link][02_Javascript]

The entire script is written on this line so scrolling further we eventually get a github gist link:  
https://gist.github.com/0xcpu/de7c4c11b59c947bc247ae6d71c9348f  
It should be noted that at the time this gist was called `pandagif.txt`, and it was later changed to just `panda.txt` during the event. The gist contains a bunch of base64 encoded test, or rather an encoded image as I knew because of that. The important thing to note here though was that it was reversed - the equals signs were at the front. But stick it through a reverser and then convert it to a gif and we get our flag.

![timctf{h4ck_for_4_l1v1ng_pl4net}][03_Flag]


[00_Display]: ../images/00_00_display.png
[01_Javascript]: ../images/00_01_javascript.png
[02_Javascript]: https://www.gnostice.com/nl_article.asp?id=310&t=An_Acrobat_Javascript_primer_with_simple_PDF_examples
[03_Flag]: image.jpg
