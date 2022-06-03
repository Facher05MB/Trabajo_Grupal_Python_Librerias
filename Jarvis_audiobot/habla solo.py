import pyttsx3
from translate import Translator
import pyjokes

engine= pyttsx3.init()
voz_t= engine.getProperty('voices')
engine.setProperty('voice',voz_t[0].id)



languages = ['es']
bromas= pyjokes.get_joke()
print("te cuento un chiste")
engine.say("te cuento un chiste")
engine.runAndWait()

def talk(audio):
    engine.say(audio)
    engine.runAndWait()





for language in languages:
    translator = Translator(to_lang=language)
    translation = translator.translate(bromas)
    audio=(f'{translation}')
    engine.runAndWait()
    talk(audio)

 