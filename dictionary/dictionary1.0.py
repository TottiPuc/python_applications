#diccionario con base de datos mysql
import mysql.connector
from difflib import get_close_matches

#conexion con mysql
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database ="ardit700_pm1database"
)

#inicio 
cursor = con.cursor()
word = input("Enter a word: ")
# realizar las consultas
def consultas_correcta(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
    results = cursor.fetchall()
    return results

def consulta_incorrecta(word):
    query2 = cursor.execute("SELECT Expression FROM Dictionary")
    results2 = cursor.fetchall()
    key = [i[0] for i in results2]
    return key

output_correcta = consultas_correcta(word)

if output_correcta: # se verifica si el resultado de la query no es una lista vacia si es vacia o la palabra no existe results sera false
    for result in output_correcta:
        print("{} ==> {}".format(result[0],result[1]))
elif len(get_close_matches(word, consulta_incorrecta(word), cutoff=0.7))>0:
    key = consulta_incorrecta(word)
    newWord = input("Did you mean {} instead? [y/n]: ".format(get_close_matches(word, key, cutoff=0.7)[0]))
    if newWord == "y":
        new = consultas_correcta(get_close_matches(word, key, cutoff=0.7)[0])
        for result in new:
            print("{} ==> {}".format(result[0],result[1]))
    elif newWord== "n":
        print("So. this word does not exist.")
    else:
        print("I do not understand")
else:
    print("This word does not exist.")