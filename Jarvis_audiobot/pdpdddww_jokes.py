from fnmatch import translate
import pyjokes
from translate  import Translator

languages = ['es']
bromas= pyjokes.get_joke()
broma = input('what is your name? ')

for language in languages:
    translator = Translator(to_lang=language)
    translation = translator.translate(bromas)
    print(f'{translation}')
 
 
 
 
 
 
# from jokes.jokes import *

#from joke import joke

#result= joke.random()

#print(result["question"])
#print(result["asnwer"])