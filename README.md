# A Basic Tutorial on How to Build a Website with Flask
**By Patrick L. Cavins**



### page_1.py
This is basic python using some basic tools in Flask

1. If you have not used Flask before you need to install it via the terminal `pip install flask` should do the trick
2. Open your IDE of choice, I like using either ATOM or VSCode

`from flask import Flask, render_template` is the only import you will need for this simple website.

If you are new to website development like I am, you are going to see some unfamiliar variable and symbols. Let's review them!

- ``@app.route('/')``: This is a decorator, when placed on top of function we call it a route. You can think of it as serving as a pointer for the information that follows. By establishing new routes, you can point to different URLs on your website.
  
- `__name__`: It is an automatically defined Python variable, required for making Flask apps. It will evaluate to the name of the current module. More on this later, but it  essentially checks to see if the file is being called from another script. [EXAMPLE](https://www.geeksforgeeks.org/__name__-special-variable-python/)  

-



### layout.html


## Resources
- Seattle Data Guy has a great tutorial on getting started with [Flask](https://medium.com/better-programming/building-your-first-website-with-flask-part-1-903a8b44e806)



## Have Questions?
Tweet me [@PatrickCavins](www.twitter.com/patrickcavins)
