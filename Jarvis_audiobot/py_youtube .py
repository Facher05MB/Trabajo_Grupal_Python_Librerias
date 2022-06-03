import speech_recognition as sr
import pyttsx3
import py_youtube as py
from py_youtube import Search

listener = sr.Recognizer()
engine = pyttsx3.init()
name  = 'Alex'                                 #nombre de quien quieres que le diga
voz_t= engine.getProperty('voices')
engine.setProperty('voice',voz_t[0].id)

#for voz in voz_t:
#    print(voz)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
    

engine.say("buenos dias")
engine.runAndWait()

def ecuchar():
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = listener.listen(source)
            print("Done!")
            text = listener.recognize_google(audio)
            rec = listener.recognize_google(audio)
            if name in rec:
                rec = rec.replace(name,'')
                talk(text)
                print(text)
            else :
                talk("a quien le hablas")
            print(text)
    except:
        pass
    return rec

def run():
    rec = ecuchar()
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        talk('reproduciendo' +rec)
        videos = Search(rec).videos()
        print(videos)       
        
        
run()