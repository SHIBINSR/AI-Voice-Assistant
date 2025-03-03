from playsound import playsound
import eel

@eel.expose
def playAssistantSound():
    music_dic = "frontend/assests/audio/start_sound.mp3"
    playsound(music_dic)
