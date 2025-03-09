import pyttsx3
import speech_recognition as sr
import eel
import time
import datetime

from engine.config import ASSISTANT_NAME
# import wikipedia
# import os

def wishme():
    time = datetime.datetime.now()
    if time.hour >= 0 and time.hour < 12:
        speak("good morning sir,how can i assist you")
    elif time.hour >= 12 and time.hour < 15:
        speak("good afternoon sir,how can i assist you")
    else:
        speak("good evening sir,how can i assist you")

def split_text_into_chunks(text, max_length=100):
    words = text.split()
    chunks = []
    current_chunk = []
    for word in words:
        if len(" ".join(current_chunk)) + len(word) + 1 > max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
        else:
            current_chunk.append(word)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',125)
    chunks = split_text_into_chunks(text)
    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()
        engine.stop()  # Ensure cleanup
        del engine

@eel.expose
def takeCommands():
    r = sr.Recognizer()
    query = None  # Ensure query is defined
    with sr.Microphone() as source:
        r.pause_threshold = 1.8
        print("Listening...")
        eel.DisplayMessage("Listening....")
        try:
            audio = r.listen(source)         
            print("Recognizing...")
            eel.DisplayMessage("Recognizing....")
            query = r.recognize_google(audio)  # Use Google's API instead of Google Cloud
            eel.DisplayMessage(query)
            print(f"Recognized: {query}")
            speak(query)
            time.sleep(3)   
        except sr.UnknownValueError:
            print("Sorry, I did not understand Please say that again.")
        except sr.RequestError as e:
            print(f"Error with the recognition service: {e}")
    return query or "No input received"

@eel.expose
def allCommands():
    query = takeCommands().lower()
    print(query)
    try:
        if "open" in query:
            from engine.features import openCommand      
            openCommand(query)

        elif "play " in query :
            from engine.features import playOnYoutube      
            playOnYoutube(query)
            
        else:
            speak("Sorry, I didn't understand that, plz try again..")
    except:
        print("a error found")
    eel.ShowHood()

    

    

    # elif "who is " in query or "wikipedia" in query:
    #     query = query.replace("who is ", "").replace("wikipedia", "")
    #     summary = wikipedia.summary(query, sentences=2)
    #     speak(summary)

    # 

    
    
   

    

