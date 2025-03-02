import os
import eel
import webbrowser

eel.init("frontend")

webbrowser.open("http://localhost:8000/index.html")

eel.start('index.html', mode=None, host='localhost', block=True)
 