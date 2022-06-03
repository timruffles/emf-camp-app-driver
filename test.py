from apps.yourapp import Yourapp

# manually run your app like the framework would
app = Yourapp()

app.on_activate()
for i in range(5):
    app.update()
app.on_deactivate()
