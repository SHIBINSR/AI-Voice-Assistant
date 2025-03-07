import pyttsx3
import speech_recognition as sr
import eel
import time
import datetime
import webbrowser
import wikipedia
import pywhatkit

def wishme():
    time = datetime.datetime.now()
    if time.hour >= 0 and time.hour < 12:
        speak("good morning sir,how can i help you")
    elif time.hour >= 12 and time.hour < 15:
        speak("good afternoon sir,how can i help you")
    else:
        speak("good evening sir,how can i help you")

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
            time.sleep(4)
            eel.ShowHood() 
        except :
            speak("Sorry I did not understand Please say that again.")
            # print(e)
         
    return query.lower() 

@eel.expose
def allCommands():
    query = takeCommands().lower()
    print(query)

    if "open google" or "chrome"  in query:
        speak("opening google.com...")
        webbrowser.open("google.com")
    elif "open youtube" in query:
        speak("opening youtube..")
        webbrowser.open("youtube.com")
    elif "who is " in query or "wikipedia" in query:
        query=query.replace("who is",'')
        query=query.replace("wikipedia","")
        summary=wikipedia.summary(query,sentences = 2) 
        speak(summary)
    elif "play " or "song " or "youtube" in query:
        summary=pywhatkit.playonyt(query)


