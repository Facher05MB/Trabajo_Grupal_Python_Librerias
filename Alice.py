import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from translate import Translator

# name of the virtual assistant
name = 'coro'

# your api key
key = 'YOUR_API_KEY_HERE'

# the flag help us to turn off the program
flag = 1

languages = ['es']
listener = sr.Recognizer()
broma = pyjokes.get_joke()
engine = pyttsx3.init()

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    '''
        here, virtual assistant can talk
    '''
    engine.say(text)
    engine.runAndWait()

def listen():
    '''
        The program recover our voice and it sends to another function
    '''
    flag = 1
    try:
        with sr.Microphone() as source:
            talk("Diga orden")
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            print (rec)
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag

def run(rec):
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec:
        order = rec.replace('search', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'salir' in rec:
        flag = 0
        talk("Saliendo...")
    elif 'noticias' in rec:
       webbrowser.open_new("https://www.google.com.ar/search?q=noticias&hl=es&sxsrf=ALiCzsYPYEwLQY2lsvep8V1HBTXKxj2X6A:1654226547578&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjB5PuNqpD4AhVbjZUCHY1QAa4Q_AUoAXoECAIQAw&biw=1366&bih=625&dpr=1")
    elif 'cuentame un chiste' in rec:
        for language in languages:
            traduccion = Translator(to_lang=language)
            translation = traduccion.translate(broma)
            talk(f'{translation}')
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag

while flag:
    flag = listen()
        
        
run()