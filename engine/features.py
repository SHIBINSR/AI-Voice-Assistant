from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
from engine.command import speak


@eel.expose
def playAssistantSound():
    music_dic = "frontend/assests/audio/start_sound.mp3"
    playsound(music_dic)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("open","")
    query.lower()

    
