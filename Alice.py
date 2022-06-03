import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia as wiki
import pyjokes
from translate import Translator

languages = ['es']
listener = sr.Recognizer()
broma = pyjokes.get_joke()
engine = pyttsx3.init()
name  = 'Axel'                                 #nombre de quien quieres que le diga
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
            print(audio)
            text = listener.recognize_google(audio)
            rec = listener.recognize_google(audio)
            if name in rec:
                rec = rec.replace(name,'')
                talk(text)
                print(text)
    except:
        pass
    return rec

def run():
    rec = ecuchar()
    if 'Reproduce' in rec:
        music = rec.replace('reproduce','')
        talk('reproduciendo' +rec)
        pywhatkit.playonyt(music)
    if 'Que hora es' in rec:
        hora = datetime.datetime.now().strftime("%I:%M %p")
        talk('son las' + hora)
    if 'Busca' in rec:
        busca = rec.replace('busca','')
        wiki.summary(busca, 1)
        talk('buscando' +rec)
    if 'cuentame un chiste' in rec:
        for language in languages:
            traduccion = Translator(to_lang=language)
            translation = traduccion   .translate(broma)
            talk(f'{translation}')
        
        
        
run()