
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
nombre = 'Rodrigo'

voz_t= engine.getProperty('voices')
engine.setProperty('voice',voz_t[0].id)

#for voz in voz_t:
#    print(voz)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
    

engine.say("buenos dias")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Say something!")
        audio = listener.listen(source)
        print("Done!")
        text = listener.recognize_google(audio)
        rec = listener.recognize_google(audio)
        if nombre in rec:
            talk(text)
        else :
            talk("a quien le hablas")
        print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio") 
