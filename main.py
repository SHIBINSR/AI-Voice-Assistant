import os
import eel
import webbrowser
from engine.features import *
from engine.command import *

def start():
    eel.init("frontend")
    playAssistantSound()
    webbrowser.open("http://localhost:8000/index.html")
    wishme()
    eel.start('index.html', mode=None, host='localhost', block=True)
 