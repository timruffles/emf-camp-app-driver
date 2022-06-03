# EMF Camp 2022 - TiDAL badge framework

I found it quite slow to iterate on TiDAL badge code, so
wrote my app against a 'driver'. Locally the driver simply
prints out the things it should do; on the device itself
you use real_driver.py instead. You implement all the commands
you want in real_driver.py.

I'm not a python programmer. It worked on python 2.7 and 3 - three
is the one to use for microppython. Sorry for any issues you encounter,
PRs accepted!