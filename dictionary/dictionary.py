import json
# cargar datos de archivo json
data = json.load(open("data.json"))

# funcion que retorna el significado de la palabra digitada por el usuario
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "this word does not exist"

word = input("Enter a word: ")

print(translate(word))