import os
import eel
import webbrowser
from engine.features import *
from engine.command import *

eel.init("frontend")

playAssistantSound()

webbrowser.open("http://localhost:8000/index.html")

wishme()
# speak("ffsfsdfsfsdfsdfsf sfsfsfsfffsfsfsfsdfsfsdfsdf sdfsfsfsdgfsgfsffgsdfsjfhsg jshgjshfjsdhgfshgfshf shfshfjshf")

eel.start('index.html', mode=None, host='localhost', block=True)
 