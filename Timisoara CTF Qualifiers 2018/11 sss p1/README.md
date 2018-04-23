### SSS - Part 1
75 points
> 3 math teachers agreed to a common secret password to access the exam answers. Luckily, one of them lost a note that seems related. They also talk all the time about some guy named Lagrange.
>
> NOTE: the coordinates are:  
> 4612c90f5d8cd5d616193257336d92af1f66df92443b4ee69f5c885f0173ad80113844e393d194e3  
> 8c25921e46b03e48b7cbe94c3267f41adf618abd16422f660b59df6fae81e8aff2242852be33db49  
> d2385b2d2fd3a6bb597ea041316255869f5c35e7e8490fe5775736805b9023dfd3100bc1e89621af  

---

![note.png][00_Note]

We get given this image, `note.png`, that shows a line and 3 points on that line, with coordinates. With a bit of googling I found out the title refers to Shamir's Secret Sharing, a way to split some secret into multiple parts that have to be combined to get the secret back, and offer no hint to the secret alone.

To Shamir's Secret Sharing it you first pick how many parts you want to have to have to get the message back, N. You then create a (N-1)th degree polynomial with random coefficients. That is, a line in the format: `y = ax^(N-1) + bx^(N-2) ... sx + t`, where a-s are all random numbers. You then set the constant, t in this case, to be your secret, decoded into an integer. Then you can pick any arbitrary points on the polynomial and use those as your keys.

So given that our image shows a line (a first degree polynomial), let's assume N=2. This also happens to make it really easy to work out the formula of the line, but we don't actually need that. Luckily, our three keys are at x positions 1, 2, and 3, so if we work out the gradient we just need to subtract that from the first key to get the secret. Once we have the secret we just need to turn it back into a string and there's our code.

```
t@t:~$ python decode.py
timctf{b4s1C_l4gr4ng3_1NTerP0LatioN}
```


[00_Note]: note.png
