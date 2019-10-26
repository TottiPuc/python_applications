import json
from difflib import get_close_matches # metodo usada para comparación de textos

# cargar datos de archivo json
data = json.load(open("data.json"))

# funcion que retorna el significado de la palabra digitada por el usuario
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.6)) > 0: # verifivar si existen coincidencias 
        return "Did you mean: {} instead?".format(get_close_matches(word, data.keys(), cutoff=0.6)[0])
    else:
        return "this word does not exist"

word = input("Enter a word: ")

print(translate(word))