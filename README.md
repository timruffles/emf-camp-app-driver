# EMF Camp 2022 - TiDAL badge framework

I found it quite slow to iterate on TiDAL badge code, so
wrote my app against a 'driver'. The driver is responsible
for everything that requires the tidal runtime environment.
The local implementation of driver simply
prints out the things it should do; on the device itself
you use real_driver.py instead. You implement all the commands
you want in real_driver.py.

I'm not a python programmer. It worked on python 2.7 and 3 - three
is the one to use for microppython. Sorry for any issues you encounter,
PRs accepted!

Here's a demo of the output. The app displays "tick 1" ... "tick $N"
in orange when run on the TiDAL.

```
ƒ python3 test.py
Yourapp defined ok
on_activate
run_ticker
fill BLACK
text tick 1 10 60 BRAND_ORANGE
fill BLACK
text tick 2 10 60 BRAND_ORANGE
fill BLACK
text tick 3 10 60 BRAND_ORANGE
fill BLACK
text tick 4 10 60 BRAND_ORANGE
fill BLACK
text tick 5 10 60 BRAND_ORANGE
on_activate
stop_ticker
```

## Setup

Put the apps/yourapp structure onto your TiDAL (ensure
you have the apps/__init__.py present too).

From the root of this repo, copy the `*driver.py` files
into the root of your tidal. You'll iterate on `real_driver.py` as you need
more real TiDAL functionality, and perhaps add more sophisticated
fake implementations in the `fake_driver.py` that is only used
on your machine.