from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
from engine.command import speak
import webbrowser
import subprocess
import pywhatkit
import struct
import time
import pvporcupine
import pyaudio


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
   
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    ACCESS_KEY = "Sk+IDWn8gh0iIuOKol/3XcKQT1C8R4p6NY4uwjGmz1Q5tohIOp612Q=="
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(
            access_key=ACCESS_KEY,
            keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except :
        
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()