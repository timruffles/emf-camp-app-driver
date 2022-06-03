from __future__ import print_function

class Driver:
    def __init__(self, app):
        self.app = app

    def command(self, name, *args):
        print(name, *args)

