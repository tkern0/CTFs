### Deery
20 points
> Hello there you handsome! Come and join us!
>
> http://deery.woodlandhighschool.xyz/

---

When you first load up the site you get greeted with a pretty standard page. But the moment you try click on anything you end up in an infinite loop of alerts. Once quick inspect element later I found what was causing it.

```javascript
function dontUDare(){
    document.onmousedown=function(event){
        while(true) {
            alert("Don't poke me like that");
            alert("Go away, I'm too shy...");
            alert("No...");
            alert("I said no...");
        }
    }
}
```

So I made a quick local copy and removed that so that I could explore further. As it turns out that was completely unnecessary, nothing on the page links anywhere or activates anything. It did let me do a whole project search for "timctf" though, and wouldn't you know what I found?

![timctf{Woodland_highschool_rocks_in_2018}][00_Flag]


[00_Flag]: ../images/04_00_flag.png
