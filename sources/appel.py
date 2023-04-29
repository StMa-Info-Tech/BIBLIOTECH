import nfc
#pip install pyscard

from time import sleep
from tkinter import *
import ujson
import ujson
with open('baseapp.json') as data_file:
    data = ujson.load(data_file)
print(data)



def get_id():

    while True:
        try:
            reader = nfc.Reader()
            data=reader.get_uid()
            if data:
                return(data)
        except:
            pass

def appel(event):

    data2=data["NSIterm"].copy()
    prof=str(get_id())
    print(prof)
    prof_id=data["prof"]
    texte.set("Bienvenue, M.Leroy")
    fenetreappel.update()
    cont=(prof==prof_id)
    print(cont)
    while cont:
        eleve_id=str(get_id())
        for key,val in data["NSIterm"].items():
            if eleve_id==val and key in data2.keys():
                texte.set("Bonjour, "+key)
                fenetreappel.update()
                data2.pop(key)
                print(data2)
        if  eleve_id==prof_id or len(data2)==0:
            cont=False
    texte.set("Les absents sont:")
    fenetreappel.update()
    sleep(2)
    absents=""
    for key in data2.keys():
            absents=absents+key+"\n"
    texte.set(absents)


fenetreappel = Tk()
texte=StringVar()
texte.set("Appuyez sur Entrée puis identifiez-vous.")
label = Label(fenetreappel, textvar=texte)
label.pack()
fenetreappel.bind("<Return>", appel)
fenetreappel.mainloop()
