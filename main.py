import os
import eel
import webbrowser
from engine.features import *

eel.init("frontend")

playAssistantSound()

webbrowser.open("http://localhost:8000/index.html")

eel.start('index.html', mode=None, host='localhost', block=True)
 