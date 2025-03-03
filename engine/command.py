import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate',100)

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
    chunks = split_text_into_chunks(text)
    print(f"jarvis : {text}")
    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()
    
def take_commands():
    r = sr.Recognizer()
    query = None  # Ensure query is defined
    with sr.Microphone() as source:
        r.pause_threshold = 1.8
        print("Listening...")
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio)  # Use Google's API instead of Google Cloud
            print(f"Recognized: {query}")
        except sr.UnknownValueError:
            speak("Sorry I did not understand Please say that again.")
            return ""
    return query    
    

