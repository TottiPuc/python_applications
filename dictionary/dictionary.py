import json
from difflib import get_close_matches # metodo usada para comparación de textos

# cargar datos de archivo json
data = json.load(open("data.json"))

# funcion que retorna el significado de la palabra digitada por el usuario
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: # nueva funcionalidad verifica si hay nombres propios que empiezan por mayusculas 
        return data[word.title()]
    elif word.upper() in data: # condicional para buscar acronimos
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.6)) > 0: # verifivar si existen coincidencias 
        newWord = input("Did you mean: '{}' instead? [y/n]".format(get_close_matches(word, data.keys(), cutoff=0.6)[0]))
        if newWord == "y":
            return data[get_close_matches(word, data.keys(), cutoff=0.6)[0]]
        elif newWord == "n":
            return "this word does not exist, please enter a correct word." 
        else:
            return "I did not understand your entry"        
    else:
        return "this word does not exist"

word = input("Enter a word: ")

out = translate(word)

# verificando el tipo de salida

if type(out) == str:
    print(out)
else:
    for i in out:
       print("==> {}".format(i))