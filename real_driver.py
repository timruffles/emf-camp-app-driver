# On your TiDAL, change driver.py to use this implementation

# everything you want to do with the tidal/board APIs, do in here.
# that way you don't need to import anything that's not going to be
# present on your machine
import tidal
import vga2_16x32 as default_font

class Driver:
    def __init__(self, app):
        self.app = app
        tidal.set_display_rotation(180)

    def command(self, name, *args):
        return getattr(self, name)(*args)

    def text(self, text, x, y, color):
        tidal.display.text(default_font, text, x, y, color)

    def fill(self, color):
        tidal.display.fill(color)

    def run_ticker(self):
        self.timer = self.app.periodic(500, self.app.update)

    def stop_ticker(self):
        self.timer.stop()

# I found I didn't get syntax errors, so this is a sanity check
print("Driver defined ok")