import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia as wiki


listener = sr.Recognizer()
engine = pyttsx3.init()
name  = 'Axel'                           #nombre de quien quieres que le diga
pregunta = 0
voz_t= engine.getProperty('voices')
engine.setProperty('voice',voz_t[0].id)

for voz in voz_t:
   print(voz)

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
            print(text)
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio") 
    return rec

def run():
    rec = ecuchar()

    if 'que hora es' in rec:
        hora = datetime.datetime.now().strftime("%I:%M %p")
        talk('son las' + hora)
        pregunta = 1
        
    if 'Busca' in rec:
        
        busca = rec.replace('Busca','')
        wiki.summary(busca, 1)
        talk('buscando' +rec)
        pregunta = 1
        print(busca)
        
    if 'cuentame un chiste' in rec:
        talk('que le dijo un pez a otro pez')
        engine.runAndWait()
        talk('nada')
        
    if 'Summa' in rec:
        with sr.Microphone() as num:
            talk ('dime el primer numero')
            print('dime el primer numero')
            primer_num = listener.listen(num)
            engine.runAndWait()
        with sr.Microphone() as num2:
            talk ('dime el segundo numero')
            print('dime el segundo numero')
            segundo_num = listener.listen(num2)
            engine.runAndWait()
        suma =  primer_num + segundo_num
        talk('el resultado da' + suma)
        print(suma)
            
        
                
run()