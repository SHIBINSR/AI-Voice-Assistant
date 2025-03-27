from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
from engine.command import speak
import webbrowser
import datetime
import pywhatkit
import struct
import time
import pvporcupine
import pyaudio
from hugchat import hugchat

def get_time():
    now = datetime.datetime.now()
    date=now.strftime("Today is %A, %d %B %Y, and the time is %I:%M %p.")
    print(date)
    # eel.DisplayMessage((date))
    speak(date)

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
            # eel.DisplayMessage("Opening Terminal....")
            speak("Opening terminal..")
            os.system("gnome-terminal")  
        except Exception as e:
            print(e)

    elif "text editor" in query:
        # eel.DisplayMessage("Opening Text editor....")
        speak("Opening text editor..")
        os.system("gedit")
       
    elif "brave" in query:
        # eel.DisplayMessage("Opening brave....")
        speak("Opening brave...")
        os.system("brave-browser")

    elif "google" in query or "chrome" in query:
        # eel.DisplayMessage("Opening Google chrome....")
        speak("Opening Google chrome...")
        webbrowser.open("https://google.com")

    elif "youtube" in query:
        # eel.DisplayMessage("Opening youtube....")
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")

    else:
        # eel.DisplayMessage(f"The Application {query} not found")
        speak(f"The Application {query} not found")
        print("App not found!")

def playOnYoutube(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("play","")
    query = query.replace("on youtube","")
    query = query.replace("can you","")
    query.lower()
    eel.DisplayMessage(f"Playing {query} on Youtube...")
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

# chat bot 
def chatBot(query):
    # print(query)j
    try:
        eel.DisplayMessage(query)
        eel.DisplayMessage("Loading...")
        user_input = query.lower()
        chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
        # id = chatbot.new_conversation()
        # chatbot.change_conversation(id)
        response = chatbot.chat(user_input)
        # print("response-----------",response)
        words = str(response).replace("*", "").strip()  # Clean response
        # print("words-------------",words)
        sentences = words.split(". ")  # Split at period and space
        # print("sentence--------------",sentences)
        short_response = ". ".join(sentences[:2])
        # print("short response---------",response)
        if not short_response.endswith("."):  
            short_response += "."
        print("chat bot response:",short_response)
        # eel.DisplayMessage(short_response)
        speak(short_response)
        return response
    except Exception as e:
        print(f"Chatbot error: {e}")
        return "I'm sorry, something went wrong."

