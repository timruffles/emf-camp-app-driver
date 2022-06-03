# name this 'driver.py' on your machine. This has no imports
# from tidal so everthing will work locally in test.py
from __future__ import print_function

class Driver:
    def __init__(self, app):
        self.app = app

    def command(self, name, *args):
        print(name, *args)

