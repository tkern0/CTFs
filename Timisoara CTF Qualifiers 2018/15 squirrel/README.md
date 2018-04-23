### Squirrels
100 points
> This is the final version!
> 
> http://squirrels.woodlandhighschool.xyz/

---

Visiting this site looks a lot like the last two in this series. This time it's running on ordinary http and there's nothing hiding in the scripts. Because there's nothing to be found on the side I tried accessing other pages.

```
/flag        -  404 Not Found
/flag.html   -  404 Not Found
/flag.txt    -  404 Not Found
/robots.txt  -  404 Not Found
/admin       -  404 Not Found
/.git        -  403 Forbidden
```

That's interesting. I went into one of my own repositories and checked what some of the files in there were, and then tried `http://squirrels.woodlandhighschool.xyz/.git/HEAD`. What do you know, it worked, I got the file. At this point I remembered a video I'd seen on a challenge where you had to download the .git folder like this, and with a bit of googleing I found [this][GitTools]. So I just had to run `./gitdumper.sh http://squirrels.woodlandhighschool.xyz/.git/ /squirrel` and I quickly had the repository. But then what? The repository only had a single commit, nothing in old versions to exploit.

```
t@t:~/squirrel$ git log
commit 0d68a6f3cd28bb3572cb1ae6f21706570e76b4f3
Author: Squirrels <squirrels@woodlandhighschool.com>
Date:   Thu Apr 12 13:43:01 2018 +0300

    Initial version
t@t:~/squirrel$
```

Well poking through the .git files a bit I found something interesting, in 'config'

```
[remote "fork"]
    url = http://git.woodlandhighschool.xyz/squirrels
    fetch = +refs/heads/*:refs/remotes/fork/*
```

So I tried `git pull fork master`. And it starts up perfectly fine, downloads all the objects... and then has a merge conflict. Thing is we still get `index.html`, and if you look through that:

```
=======
        <p>timctf{g1t_w1z4rd_1n_w00dl4and_h1ghsch00l}</p>
  </div>
```


[GitTools]: https://github.com/internetwache/GitTools
