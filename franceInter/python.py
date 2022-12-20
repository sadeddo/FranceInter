import json
from tkinter import image_names
from quickstart_file import personCount
from speech_synthesis import speech

with open('fichier.json') as fichier:
    data = json.load(fichier)

message = (data['message'])
nombre_max = (data['nombre'])
nomImage = (data['image'])
 
def main(message,nombre_max,nomImage):
    nbrImage = personCount(nomImage)
    if (nbrImage > int(nombre_max)):
        print('ok')
        speech(message)
    else:
        print('non')
        
main(message,nombre_max,nomImage)