from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
from engine.command import speak
import webbrowser
import subprocess
import pywhatkit


@eel.expose
def playAssistantSound():
    music_dic = "frontend/assests/audio/start_sound.mp3"
    playsound(music_dic)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("open","")
    query.lower()
    
    if "open terminal" == query :
        try:
            speak("Opening terminal..")
            os.system("gnome-terminal")  
        except Exception as e:
            print(e)

    elif "text editor" in query:
        speak("Opening text editor..")
        os.system("gedit")
       
    elif "brave" in query:
        speak("Opening brave ..")
        os.system("brave-browser")

    elif "open google" in query or "chrome" in query:
        speak("Opening Google chrome...")
        webbrowser.open("https://google.com")

    elif "open youtube" in query or "youtube" in query:
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")

    else:
        speak(f"The Application {query} not found")
        print("App not found!")

def playOnYoutube(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("play","")
    query = query.replace("on youtube","")
    query.lower()
    speak(f"Playing {query} on YouTube...")
    pywhatkit.playonyt(query)
   