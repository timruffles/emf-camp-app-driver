import tidal
from app import App
from apps.yourapp import driver

# define your app here. When you need to do anything with tidal, import
class Yourapp(App):
    def on_activate(self):
        print("on_activate")
        super(Yourapp, self).on_activate()
        self.driver = driver.Driver(self)
        self.ticks = 0
        self.driver.command("run_ticker")

    def update(self):
        self.driver.command("fill", tidal.BLACK)
        self.ticks += 1
        self.driver.command("text", "tick %d" % self.ticks, 10, 60, tidal.BRAND_ORANGE)

    def on_deactivate(self):
        print("on_activate")
        super(Yourapp, self).on_deactivate()
        self.driver.command("stop_ticker")

main = Yourapp
print("Yourapp defined ok")