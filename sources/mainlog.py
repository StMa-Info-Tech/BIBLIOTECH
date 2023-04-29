import nfc
from time import sleep
from sqlite3 import *
from datetime import date, timedelta
from tkinter import *
from PIL import ImageTk, Image
from isbnlib import *
import isbnlib
import urllib.request
from isbnlib.registry import bibformatters

root = Tk()
connexion = connect('bibliotheque.db')
today_date = date.today()
td = timedelta(30)
curseur = connexion.cursor()
### initialisation des label/image/boutton commun
image21= ImageTk.PhotoImage(Image.open('annexe\icon3.jfif').resize((50,50)))
image31 = ImageTk.PhotoImage(Image.open('annexe\icon4.jpg').resize((30, 30)))
################################################################################
def get_id():

    while True:
        try:
            reader = nfc.Reader()
            data = reader.get_uid()
            if data:
                return(data)
        except:
            pass
################################################################################
def menu():
    fenetre.pack_forget()
    fenetre2.pack_forget()
    fenetre3.pack_forget()
    fenetre4.pack_forget()
    fenetre5.pack_forget()
    fenetre5.pack_forget()
    fenetre6.pack_forget()
    fenetre7.pack_forget()
    fenetre8.pack_forget()
    fenetre9.pack_forget()
    fenetre10.pack_forget()
    frametri.pack_forget()
    fenetre1.pack()
################################################################################
frametri= Frame(root)
update= {"adherent":"nomAdherent,prenomAdherent,adresse,telephone","livre":"isbn,titre,auteur,editeur"}
updateid= {"adherent":"identifiant","livre":"idlivre"}
truc=[]
def trie():
    labelnomtrie.grid(row=3,column=2)
    labeladresbntrie.grid(row=3,column=3)
    labelprenomauteurtrie.grid(row=3,column=4)
    labelediteurteltrie.grid(row=3,column=5)
    labelidtrie.grid(row=3,column=1)
    labelidtrielab.grid(row=2, column=1)
    labelnomtrielab.grid(row=2,column=2)
    labeladresbntrielab.grid(row=2,column=3)
    labelprenomauteurtrielab.grid(row=2,column=4)
    labelediteurteltrielab.grid(row=2, column=5)
    boutonupdate.grid(row=3, column=6)
    truc= get_id()
    islivre=False
    isadh=False
    try :
        truc[0]
        print("a")
        try:
            truc[6]
            islivre=True
            isadh=False
        except:
            islivre=False
            isadh=True
        print('d')
        if isadh==True and islivre==False:
            selectrie='SELECT * FROM adherent where identifiant="'+str(truc)+'"'
            listrie= curseur.execute(selectrie)
            listrie= listrie.fetchone()
            idtrie.set(str(listrie[0]))
            idtrieget.set(listrie[0])
            nomtrie.set(str(listrie[2]))
            adresbntrie.set(str(listrie[3]))
            prenomauteurtrie.set(str(listrie[1]))
            editeurteltrie.set(str(listrie[4]))
            idtrielab.set("Id de l'adherent")
            nomtrielab.set("Prenom de l'adherent")        #2
            adresbntrielab.set("Adresse")                 #3
            prenomauteurtrielab.set("Nom de l'adherent")  #1
            editeurteltrielab.set("Telephone")            #4
        if isadh==False and islivre==True:
            selectrie='SELECT * FROM livre where idlivre="'+str(truc)+'"'
            listrie= curseur.execute(selectrie)
            listrie= listrie.fetchall()
            listrie=listrie[0]
            idtrie.set(str(listrie[4]))
            nomtrie.set(str(listrie[1]))
            adresbntrie.set(str(listrie[2]))
            prenomauteurtrie.set(str(listrie[0]))
            editeurteltrie.set(str(listrie[3]))
            print(str(listrie[5]))
            try:
                urllib.request.urlretrieve(listrie[5],"img.jpg")
                imgcouv = ImageTk.PhotoImage(Image.open('img.jpg').resize((128, 201)))
                label611=Label(frametri,image=imgcouv).grid(row=6, column=6)
            except:
                label611=Label(frametri,text="Aucune couverture pour ce livre").grid(row=6, column=6)
            idtrielab.set("Id du livre")
            nomtrielab.set("Titre")                       #2
            adresbntrielab.set("Auteur du livre")         #3
            prenomauteurtrielab.set("Isbn")               #1
            editeurteltrielab.set("Editeur du livre")     #4
            print("b")
    except:
        print('c')
    #c= curseur.execute('select * from livre where idlivre="0"') #erreur mais c'est normal
    #c.fetchone() #erreur mais c'est normal
    #labelerreurlivre= Label(frametri, text="identifiant:"+str(c[0]),width=1) #erreur mais c'est normal
def resettri():
    labelnomtrie.grid_forget()
    labeladresbntrie.grid_forget()
    labelprenomauteurtrie.grid_forget()
    labelediteurteltrie.grid_forget()
    labelidtrie.grid_forget()
    labelidtrielab.grid_forget()
    labelnomtrielab.grid_forget()
    labeladresbntrielab.grid_forget()
    labelprenomauteurtrielab.grid_forget()
    labelediteurteltrielab.grid_forget()
    boutonupdate.grid_forget()
def updatetri():
    try:
        truc[6]
        table="livre"
    except:
        table="adherent"
    requete='UPDATE '+table+' SET ('+update[table]+')=("'+prenomauteurtrie.get()+'","'+nomtrie.get()+'","'+adresbntrie.get()+'","'+editeurteltrie.get()+'") WHERE '+ updateid[table]+'="'+idtrie.get()+'"'
    print(requete)
    curseur.execute(requete)
    connexion.commit()
idtrieget= StringVar()
idtrie=StringVar()
nomtrie=StringVar()
adresbntrie=StringVar()
prenomauteurtrie=StringVar()
editeurteltrie=StringVar()
idtrielab= StringVar()
nomtrielab= StringVar()
adresbntrielab= StringVar()
prenomauteurtrielab= StringVar()
editeurteltrielab=StringVar()
labelidtrie= Label(frametri, textvariable=idtrie)
labelnomtrie= Entry(frametri,textvariable=nomtrie)
labeladresbntrie= Entry(frametri, textvariable=adresbntrie)
labelprenomauteurtrie= Entry(frametri, textvariable=prenomauteurtrie)
labelediteurteltrie=Entry(frametri, textvariable=editeurteltrie)
labelidtrielab= Label(frametri, textvariable=idtrielab)
labelnomtrielab= Label(frametri , textvariable=nomtrielab)
labeladresbntrielab= Label(frametri, textvariable=adresbntrielab)
labelprenomauteurtrielab= Label(frametri, textvariable=prenomauteurtrielab)
labelediteurteltrielab=Label(frametri, textvariable=editeurteltrielab)
Buttontri= Button(frametri,image=image31, command=trie).grid(row=1,column=1)
bouton2 = Button(frametri,image=image21,height=50,width=50,command=menu).grid(row=1, column=7)
label04 = Label(frametri, text="Menu").grid(row=2, column=7)
boutonupdate = Button(frametri, text="update",command=updatetri)
################################################################################
fenetre = Frame(root)
prenom= StringVar()
nom= StringVar()
adresse = StringVar()
telephone= StringVar()
fixeaddadh= StringVar()
identifiant=StringVar()
def ajouter_adherent():
    l='"'+str(get_id())+'"'
    x=('"')+str(chaine00.get())+str('"')
    y=('"')+str(chaine02.get())+str('"')
    z=('"')+str(chaine03.get())+str('"')
    w=('"')+str(chaine04.get())+str('"')
    requete="INSERT INTO adherent(nomAdherent,prenomAdherent,adresse,telephone,identifiant) VALUES("+x+","+y+","+z+","+w+","+l+")"
    curseur.execute(requete)
    connexion.commit()
    prenom.set("Prenom : "+x[1:-1])
    nom.set("Nom : "+y[1:-1])
    adresse.set("Adresse : "+z[1:-1])
    telephone.set("Telephone : "+w[1:-1])
    fixeaddadh.set("Adhérent ajouté")
    label05= Label(fenetre, textvariable=fixeaddadh,width=20).grid(row=5,column=3)
    label06= Label(fenetre, textvariable=prenom,width=20).grid(row=6,column=1)
    label07= Label(fenetre, textvariable=nom,width=20).grid(row=6,column=2)
    label08= Label(fenetre, textvariable=adresse,width=20).grid(row=6,column=3)
    label09= Label(fenetre, textvariable=telephone,width=20).grid(row=6,column=4)
    requete02="select identifiant from adherent where prenomAdherent="+str(y)
    a=curseur.execute(requete02)
    a= a.fetchone()
    identifiant.set("Identifiant :"+str(a[0]))
    laebl010= Label(fenetre, textvariable=identifiant,width=20).grid(row=6,column=5)
def resetaddadh():
    fixeaddadh.set('')
    prenom.set('')
    nom.set('')
    adresse.set('')
    telephone.set('')
    identifiant.set('')
chaine00 = StringVar()
chaine00.set("Nom")
entree = Entry(fenetre, textvariable=chaine00, width=30).grid(row=3, column=1)
chaine02 = StringVar()
chaine02.set("Prénom")
entree2 = Entry(fenetre, textvariable=chaine02, width=30).grid(row=3, column=2)
chaine03 = StringVar()
chaine03.set("adresse")
entree3 = Entry(fenetre, textvariable=chaine03, width=30).grid(row=3, column=3)
chaine04 = StringVar()
chaine04.set("telephone")
entree4 = Entry(fenetre, textvariable=chaine04, width=30).grid(row=3, column=4)
bouton = Button(fenetre,image=image31,command=ajouter_adherent).grid(row=3, column=5)
label03=Label(fenetre,text="",width=10).grid(row=1,column=6)
label02= Label(fenetre, text="",width=10).grid(row=2,column=6)
label02= Label(fenetre, text="Ajouter un adhérent",width=20).grid(row=1,column=3)
bouton2 = Button(fenetre,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
label04 = Label(fenetre, text="Menu").grid(row=4, column=7)
################################################################################
fenetre6= Frame(root)
titre= StringVar()
auteur= StringVar()
editeur= StringVar()
isbn= StringVar()
idlivreadd= StringVar()
fixeaddliv=StringVar()
titreconf=StringVar()
auteurconf=StringVar()
editeurconf=StringVar()
isbnconf=StringVar()
idconf = StringVar()
isbn1=""
url=""
def ajouter_livre():
    j='"'+str(get_id())+'"'
    #j="[4, 77, 42, 10, 34, 104, 129]"
    #w='9782266282413'
    #w='9782267032185'
    w=('"')+str(chaine60.get())+('"')
    book=isbnlib.meta(w)
    auteurauto = '"'+str(book.get('Authors'))[2:-2]+'"'
    titreauto = '"'+str(book.get('Title'))+'"'
    editeurauto = '"'+str(book.get('Publisher'))+'"'
    try:
        url = cover(w)['smallThumbnail']
    except:
        url= "None"
    """
    requete="INSERT INTO livre(isbn,titre,auteur,editeur,idlivre,couv) VALUES("+w+","+titreauto+","+auteurauto+","+editeurauto+','+j+',"'+url+'")'
    print(requete)
    curseur.execute(requete)
    connexion.commit()
    """
    titreconf.set(titreauto[1:-1])
    auteurconf.set(auteurauto[1:-1])
    editeurconf.set(editeurauto[1:-1])
    isbnconf.set(w[1:-1])
    idconf.set(j)
    titre.set("Titre : "+titreauto[1:-1])
    auteur.set("Auteur : "+auteurauto[1:-1])
    editeur.set("Editeur : "+editeurauto[1:-1])
    isbn.set("Isbn : "+w[1:-1])
    idlivreadd.set("idlivre : "+j)
    fixeaddliv.set("Livre ajouté")
    label65= Label(fenetre6, textvariable=fixeaddliv,width=20).grid(row=5,column=3)
    label66= Label(fenetre6, textvariable=titre).grid(row=6,column=1)
    label67= Label(fenetre6, textvariable=auteur).grid(row=6,column=2)
    label68= Label(fenetre6, textvariable=editeur).grid(row=6,column=3)
    label69= Label(fenetre6, textvariable=isbn).grid(row=6,column=4)
    lebel610= Label(fenetre6, textvariable=idlivreadd).grid(row=6,column=5)
    try:
        urllib.request.urlretrieve(cover(w)['smallThumbnail'],"img.jpg")
        imgcouv = ImageTk.PhotoImage(Image.open('img.jpg').resize((128, 201)))
        label611=Label(fenetre6,image=imgcouv).grid(row=6, column=6)
        try:
            Labelerreurcouv.grid_forget()
        except:
            pass
    except:
        try:
            label611.grid_forget()
        except:
            pass
        Labelerreurcouv= Label(fenetre6, text="Aucune couverture trouvé pour ce livre").grid(row=6,column=6)
    BouttonConfir= Button(fenetre6, text="Confirmer", command=confirmation).grid(row=6,column=7)
    requete62='select idlivre from livre where idlivre="0"'  #erreur mais c'est normal
    c= curseur.execute('select * from livre where idlivre="0"') #erreur mais c'est normal
    c.fetchone() #erreur mais c'est normal
    labelerreurlivre= Label(fenetre6, text="identifiant:"+str(c[0]),width=1) #erreur mais c'est normal
def resetaddliv():
    fixeaddliv.set('')
    titre.set('')
    auteur.set('')
    editeur.set('')
    isbn.set('')
    idlivreadd.set('')
    try:
        Labelerreurcouv.grid_forget()
    except:
        pass
    try:
        label611.grid_forget()
    except:
        pass
def confirmation():
    w=('"')+str(chaine60.get())+('"')
    j="[4, 77, 42, 10, 34, 104, 129]"
    url=""
    requete='INSERT INTO livre(isbn,titre,auteur,editeur,idlivre,couv) VALUES("'+str(isbnconf.get())+'","'+str(titreconf.get())+'","'+str(auteurconf.get())+'","'+str(editeurconf.get())+'","'+str(idconf.get())+'","'+url+'")'
    curseur.execute(requete)
    connexion.commit()
chaine60 = StringVar()
chaine60.set("Isbn")
entryisbn = Entry(fenetre6,textvariable=chaine60).grid(row=3,column=1)
bouton = Button(fenetre6,image=image31,command=ajouter_livre).grid(row=3, column=5)
label63=Label(fenetre6,text="",width=10).grid(row=1,column=6)
label62= Label(fenetre6, text="",width=10).grid(row=2,column=6)
label62= Label(fenetre6, text="Ajouter un livre",width=20).grid(row=1,column=3)
bouton2 = Button(fenetre6,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
label64 = Label(fenetre6, text="Menu").grid(row=4, column=7)
################################################################################
fenetre2= Frame(root)
chose= StringVar()
def trielisteadh():
    machin=chose.get()
    requete='  SELECT * FROM adherent WHERE nomAdherent like "%'+str(machin)+'%" OR prenomAdherent like "%'+str(machin)+'%" OR adresse like "%'+str(machin)+'%" OR telephone like "%'+str(machin)+'%"  '
    machinchose= curseur.execute(requete)
    machinchose= machinchose.fetchall()
    for item in fenetre2.winfo_children():
        item.destroy()
    for i in range(len(machinchose)):
        chainesel = Label(fenetre2,text=machinchose[i][0], width=15).grid(row=i+4,column=1)
        chaine7sel = Label(fenetre2,text=machinchose[i][1], width=20).grid(row=i+4,column=2)
        chaine8sel = Label(fenetre2,text=machinchose[i][2], width=20).grid(row=i+4,column=3)
        chaine9sel = Label(fenetre2,text=machinchose[i][3], width=20).grid(row=i+4,column=4)
        chaine10sel = Label(fenetre2,text=machinchose[i][4], width=20).grid(row=i+4,column=5)
    if len(machinchose)==0:
        chainesel = Label(fenetre2,text="Aucune personne ne correspond").grid(row=4,column=3)
    chaine2=Label(fenetre2,text="identifiant",width=10).grid(row=3,column=1)
    chaine3=Label(fenetre2,text="nom",width=10).grid(row=3,column=2)
    chaine4=Label(fenetre2,text="prenom",width=10).grid(row=3,column=3)
    chaine5=Label(fenetre2,text="adresse",width=15).grid(row=3,column=4)
    chaine6=Label(fenetre2,text="telephone",width=10).grid(row=3,column=5)
    label23=Label(fenetre2,text="",width=10).grid(row=1,column=6)
    label22= Label(fenetre2, text="",width=10).grid(row=2,column=5)
    label22= Label(fenetre2, text="Liste des adhérents",width=15).grid(row=1,column=3)
    bouton2 = Button(fenetre2,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label24 = Label(fenetre2, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecAdh= Entry(fenetre2, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre2, text='Trier',command=trielisteadh).grid(row=6,column=8)
    #y=len(machinchose)*200+100
    #x=900
    #root.geometry(str(x)+"x"+str(y))
def clearlisteadh():
    for item in fenetre2.winfo_children():
        item.destroy()
    requete="SELECT * FROM adherent"
    curseur.execute(requete)
    ans= curseur.fetchall()
    for i in range(len(ans)):
        chaine = Label(fenetre2,text=ans[i][0]).grid(row=i+4,column=1)
        chaine7 = Label(fenetre2,text=ans[i][1]).grid(row=i+4,column=2)
        chaine8 = Label(fenetre2,text=ans[i][2]).grid(row=i+4,column=3)
        chaine9 = Label(fenetre2,text=ans[i][3]).grid(row=i+4,column=4)
        chaine10 = Label(fenetre2,text=ans[i][4]).grid(row=i+4,column=5)
    chaine2=Label(fenetre2,text="identifiant",width=10).grid(row=3,column=1)
    chaine3=Label(fenetre2,text="nom",width=10).grid(row=3,column=2)
    chaine4=Label(fenetre2,text="prenom",width=10).grid(row=3,column=3)
    chaine5=Label(fenetre2,text="adresse",width=15).grid(row=3,column=4)
    chaine6=Label(fenetre2,text="telephone",width=10).grid(row=3,column=5)
    label23=Label(fenetre2,text="",width=10).grid(row=1,column=6)
    label22= Label(fenetre2, text="",width=10).grid(row=2,column=5)
    label22= Label(fenetre2, text="Liste des adhérents",width=15).grid(row=1,column=4)
    bouton2 = Button(fenetre2,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label24 = Label(fenetre2, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecAdh= Entry(fenetre2, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre2, text='Trier',command=trielisteadh).grid(row=6,column=8)
################################################################################
fenetre3= Frame(root)
chose= StringVar()
def trielisteemprunt():
    machin=chose.get()
    requete='  SELECT * FROM emprunt WHERE numlivre like "%'+str(machin)+'%" OR nomlivre like "%'+str(machin)+'%" OR DateEmprunt like "%'+str(machin)+'%" OR NomAdherent like "%'+str(machin)+'%"OR Identifiant like "%'+str(machin)+'%" OR NumEmprunt like "%'+str(machin)+'%" OR DateRetour like "%'+str(machin)+'%" '
    machinchose= curseur.execute(requete)
    machinchose= machinchose.fetchall()
    for item in fenetre3.winfo_children():
        item.destroy()
    for i in range(len(machinchose)):
        chainesel = Label(fenetre3,text=machinchose[i][0], width=15).grid(row=i+4,column=1)
        chaine7sel = Label(fenetre3,text=machinchose[i][1], width=20).grid(row=i+4,column=2)
        chaine8sel = Label(fenetre3,text=machinchose[i][2], width=20).grid(row=i+4,column=3)
        chaine9sel = Label(fenetre3,text=machinchose[i][3], width=20).grid(row=i+4,column=4)
        chaine10sel = Label(fenetre3,text=machinchose[i][4], width=20).grid(row=i+4,column=5)
    if len(machinchose)==0:
        chainesel = Label(fenetre3,text="Aucun livre ne correspond").grid(row=4,column=3)
    chaine2=Label(fenetre3,text="nom adherent",width=10).grid(row=3,column=1)
    chaine3=Label(fenetre3,text="titre",width=10).grid(row=3,column=2)
    chaine4=Label(fenetre3,text="dateemprunt",width=10).grid(row=3,column=3)
    chaine5=Label(fenetre3,text="dateretour",width=15).grid(row=3,column=4)
    chaine6=Label(fenetre3,text="numemprunt",width=10).grid(row=3,column=5)
    label23=Label(fenetre3,text="",width=10).grid(row=1,column=6)
    label22= Label(fenetre3, text="",width=10).grid(row=2,column=5)
    label22= Label(fenetre3, text="Liste des emprunts",width=15).grid(row=1,column=3)
    bouton2 = Button(fenetre3,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label24 = Label(fenetre3, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecAdh= Entry(fenetre3, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre3, text='Trier',command=trielisteemprunt).grid(row=6,column=8)
    #y=len(machinchose)*200+100
    #x=900
    #root.geometry(str(x)+"x"+str(y))
def clearlisteemprunt():
    for item in fenetre3.winfo_children():
        item.destroy()
    requete="SELECT * FROM emprunt"
    curseur.execute(requete)
    ans= curseur.fetchall()
    for i in range(len(ans)):
        chaine = Label(fenetre3,text=ans[i][6]).grid(row=i+4,column=1)
        chaine7 = Label(fenetre3,text=ans[i][1]).grid(row=i+4,column=2)
        chaine8 = Label(fenetre3,text=ans[i][2]).grid(row=i+4,column=3)
        chaine9 = Label(fenetre3,text=ans[i][3]).grid(row=i+4,column=4)
        chaine10 = Label(fenetre3,text=ans[i][4]).grid(row=i+4,column=5)
    chaine2=Label(fenetre3,text="Nom Adherent").grid(row=3,column=1)
    chaine3=Label(fenetre3,text="titre").grid(row=3,column=2)
    chaine4=Label(fenetre3,text="dateemprunt").grid(row=3,column=3)
    chaine5=Label(fenetre3,text="dateretour").grid(row=3,column=4)
    chaine6=Label(fenetre3,text="numemprunt").grid(row=3,column=5)
    label33=Label(fenetre3,text="",width=10).grid(row=1,column=6)
    label32= Label(fenetre3, text="",width=10).grid(row=2,column=5)
    label32= Label(fenetre3, text="Liste des emprunts",width=15).grid(row=1,column=3)
    bouton2 = Button(fenetre3,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label34 = Label(fenetre3, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecemp= Entry(fenetre3, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre3, text='Trier',command=trielisteemprunt).grid(row=6,column=8)
################################################################################
fenetre4 = Frame(root)
chose= StringVar()
def trielisteliv():
    machin=chose.get()
    requete='  SELECT * FROM livre WHERE isbn like "%'+str(machin)+'%" OR titre like "%'+str(machin)+'%" OR auteur like "%'+str(machin)+'%" OR idlivre like "%'+str(machin)+'%" OR editeur like "%'+str(machin)+'%"  '
    machinchose= curseur.execute(requete)
    machinchose= machinchose.fetchall()
    for item in fenetre4.winfo_children():
        item.destroy()
    for i in range(len(machinchose)):
        chainesel = Label(fenetre4,text=machinchose[i][0]).grid(row=i+4,column=1)
        chaine7sel = Label(fenetre4,text=machinchose[i][1]).grid(row=i+4,column=2)
        chaine8sel = Label(fenetre4,text=machinchose[i][2], width=20).grid(row=i+4,column=3)
        chaine9sel = Label(fenetre4,text=machinchose[i][3], width=20).grid(row=i+4,column=4)
        chaine10sel = Label(fenetre4,text=machinchose[i][4]).grid(row=i+4,column=5)
    if len(machinchose)==0:
        chainesel = Label(fenetre4,text="Aucun livre ne correspond").grid(row=4,column=3)
    chaine2=Label(fenetre4,text="ISBN",width=10).grid(row=3,column=1)
    chaine3=Label(fenetre4,text="Titre",width=10).grid(row=3,column=2)
    chaine4=Label(fenetre4,text="Auteur",width=10).grid(row=3,column=3)
    chaine5=Label(fenetre4,text="Editeur",width=15).grid(row=3,column=4)
    chaine6=Label(fenetre4,text="Idlivre",width=10).grid(row=3,column=5)
    label23=Label(fenetre4,text="",width=10).grid(row=1,column=6)
    label22= Label(fenetre4, text="",width=10).grid(row=2,column=5)
    label22= Label(fenetre4, text="Liste des livres",width=15).grid(row=1,column=3)
    bouton2 = Button(fenetre4,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label24 = Label(fenetre4, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecAdh= Entry(fenetre4, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre4, text='Trier',command=trielisteliv).grid(row=6,column=8)
def clearlistelivre():
    for item in fenetre4.winfo_children():
        item.destroy()
    requete="SELECT * FROM livre"
    curseur.execute(requete)
    ans= curseur.fetchall()
    for i in range(len(ans)):
        chaine = Label(fenetre4,text=ans[i][0],width=20).grid(row=i+4,column=1)
        chaine7 = Label(fenetre4,text=ans[i][1],width=80).grid(row=i+4,column=2)
        chaine8 = Label(fenetre4,text=ans[i][2],width=30).grid(row=i+4,column=3)
        chaine9 = Label(fenetre4,text=ans[i][3],width=30).grid(row=i+4,column=4)
        chaine10 = Label(fenetre4,text=ans[i][4],width=20).grid(row=i+4,column=5)
    chaine2=Label(fenetre4,text="isbn").grid(row=3,column=1)
    chaine3=Label(fenetre4,text="titre").grid(row=3,column=2)
    chaine4=Label(fenetre4,text="auteur").grid(row=3,column=3)
    chaine5=Label(fenetre4,text="editeur").grid(row=3,column=4)
    chaine6=Label(fenetre4,text="numlivre").grid(row=3,column=5)
    label43=Label(fenetre4,text="",width=10).grid(row=1,column=6)
    label42= Label(fenetre4, text="",width=10).grid(row=2,column=5)
    label42= Label(fenetre4, text="Liste des livres",width=15).grid(row=1,column=3)
    bouton2 = Button(fenetre4,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label44 = Label(fenetre4, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecAdh= Entry(fenetre4, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre4, text='Trier',command=trielisteliv).grid(row=6,column=8)
################################################################################

fenetre5 = Frame(root)
def trielisteretard():
    machin=chose.get()
    requete='  SELECT nom_livre,nom_adherent,date_retour FROM livreretard WHERE id_retard like "%'+str(machin)+'%" OR id_livre like "%'+str(machin)+'%" OR nom_livre like "%'+str(machin)+'%" OR id_adherent like "%'+str(machin)+'%"OR nom_adherent like "%'+str(machin)+'%" OR date_retour like "%'+str(machin)+'%"'
    machinchose= curseur.execute(requete)
    machinchose= machinchose.fetchall()
    for item in fenetre5.winfo_children():
        item.destroy()
    for i in range(len(machinchose)):
        chainesel = Label(fenetre5,text=machinchose[i][0]).grid(row=i+4,column=1)
        chaine7sel = Label(fenetre5,text=machinchose[i][1]).grid(row=i+4,column=2)
        chaine8sel = Label(fenetre5,text=machinchose[i][2]).grid(row=i+4,column=3)
    if len(machinchose)==0:
        chainesel = Label(fenetre5,text="Aucun livre ne correspond").grid(row=4,column=3)
    chaine2=Label(fenetre5,text="Nom du livre").grid(row=3,column=1)
    chaine3=Label(fenetre5,text="Nom de l'adherent'").grid(row=3,column=2)
    chaine4=Label(fenetre5,text="Date retour").grid(row=3,column=3)
    label23=Label(fenetre5,text="",width=10).grid(row=1,column=6)
    label22= Label(fenetre5, text="",width=10).grid(row=2,column=5)
    label22= Label(fenetre5, text="Liste des retards",width=15).grid(row=1,column=3)
    bouton2 = Button(fenetre5,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label24 = Label(fenetre5, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecAdh= Entry(fenetre5, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre5, text='Trier',command=trielisteretard).grid(row=6,column=8)
def clearlisteretard():
    pass
    for item in fenetre5.winfo_children():
        item.destroy()
    requete3='DELETE FROM livreretard WHERE id_livre != "0" '
    curseur.execute(requete3)
    requete1="SELECT NumLivre,Identifiant,dateretour,NomAdherent,NomLivre FROM emprunt WHERE dateretour < DATE()"
    a = curseur.execute(requete1)
    retard = a.fetchall()
    for i in range(len(retard)):
        requete2 ='INSERT INTO livreretard(id_livre,id_adherent,date_retour,nom_livre,nom_adherent) VALUES("'+ str(retard[i][0]) +'","'+str(retard[i][1])+'","'+str(retard[i][2])+'","'+str(retard[i][4])+'","'+str(retard[i][3])+'")'
        curseur.execute(requete2)
    requete3="SELECT * FROM livreretard"
    b = curseur.execute(requete3)
    ans= b.fetchall()
    for i in range(len(retard)):
        chaine7 = Label(fenetre5,text=retard[i][4]).grid(row=i+4,column=1)
        chaine8 = Label(fenetre5,text=retard[i][3]).grid(row=i+4,column=2)
        chaine9 = Label(fenetre5,text=retard[i][2]).grid(row=i+4,column=3)
    chaine2=Label(fenetre5,text="Nom du livre").grid(row=3,column=1)
    chaine3=Label(fenetre5,text="Nom de l'emprunteur").grid(row=3,column=2)
    chaine4=Label(fenetre5,text="date de retour").grid(row=3,column=3)
    connexion.commit()
    label53=Label(fenetre5,text="",width=10).grid(row=1,column=6)
    label52= Label(fenetre5, text="",width=10).grid(row=2,column=5)
    label52= Label(fenetre5, text="Liste des emprunt en retard",width=20).grid(row=1,column=3)
    bouton2 = Button(fenetre5,image=image21,height=50,width=50,command=menu).grid(row=3, column=7)
    label54 = Label(fenetre5, text="Menu").grid(row=4, column=7)
    chose.set('Trie')
    EntrySelecAdh= Entry(fenetre5, textvariable=chose).grid(row=6,column=7)
    BoutonTrie= Button(fenetre5, text='Trier',command=trielisteretard).grid(row=6,column=8)
################################################################################
fenetre7= Frame(root)
numlivresv= StringVar()
identifiantsv= StringVar()
dateempruntsv= StringVar()
dateretoursv= StringVar()
nomlivresv= StringVar()
nomadherentsv= StringVar()
numempruntsv= StringVar()
fixeaddemp=StringVar()
def ajouter_emprunt():
    y= get_id()
    sleep(2)
    w= get_id()
    print(y)
    print(w)
    try:
        y[6]
        d='SELECT titre FROM livre WHERE idlivre="'+str(y)+'"'
        print("1")
        a=curseur.execute(d)
        c='"'+str(a.fetchone()[0])+'"'
    except:
        d='SELECT titre FROM livre WHERE idlivre="'+str(w)+'"'
        print("2")
        a=curseur.execute(d)
        c='"'+str(a.fetchone()[0])+'"'
    try:
        y[6]
        g='SELECT nomAdherent FROM adherent WHERE identifiant="'+str(w)+'"'
        print("a")
        e=curseur.execute(g)
        f='"'+str(e.fetchone()[0])+'"'
    except:
        g='SELECT nomAdherent FROM adherent WHERE identifiant="'+str(y)+'"'
        print("b")
        e=curseur.execute(g)
        f='"'+str(e.fetchone()[0])+'"'
    td = timedelta(30)
    retour='"'+str(today_date+td)+'"'
    requete='INSERT INTO emprunt (NumLivre,identifiant,dateemprunt,dateretour,NomLivre,NomAdherent) VALUES ("'+str(w)+'","'+str(y)+'",'+'"'+str(today_date)+'"'+","+retour+","+c+","+f+")"
    curseur.execute(requete)
    connexion.commit()
    identifiantsv.set("Identifiant : "+str(y))
    numlivresv.set("Numéro du Livre : "+str(w))
    dateempruntsv.set("Date emprunt : "+str(today_date))
    dateretoursv.set("Date retour : "+retour)
    nomlivresv.set("Nom du Livre : "+c[1:-1])
    nomadherentsv.set("Nom de l'adhérent : "+f[1:-1])
    fixeaddemp.set("Emprunt Effectué")
    label65= Label(fenetre7, textvariable=fixeaddemp,width=20).grid(row=5,column=3)
    label66= Label(fenetre7, textvariable=identifiantsv,width=20).grid(row=6,column=1)
    label67= Label(fenetre7, textvariable=nomadherentsv,width=20).grid(row=6,column=2)
    label68= Label(fenetre7, textvariable=dateempruntsv,width=25).grid(row=6,column=3)
    label69= Label(fenetre7, textvariable=dateretoursv,width=25).grid(row=6,column=4)
    laebl010= Label(fenetre7, textvariable=nomlivresv,width=20).grid(row=6,column=5)
    laebl011= Label(fenetre7, textvariable=numlivresv,width=25).grid(row=6,column=6)
    requete72='select NumEmprunt from emprunt where NumLivre="'+str(w)+'"'
    print(requete72)
    b70=curseur.execute(requete72)
    b70= b70.fetchone()
    numempruntsv.set("Num Emprunt : "+str(b70[0]))
    laebl012= Label(fenetre7, textvariable=numempruntsv,width=25).grid(row=6,column=7)
def resetaddemp():
    fixeaddemp.set('')
    identifiantsv.set('')
    nomadherentsv.set('')
    dateempruntsv.set('')
    dateretoursv.set('')
    nomlivresv.set('')
    numlivresv.set('')
chaine70 = StringVar()
chaine70.set("Identifiant")
entree70 = Entry(fenetre7, textvariable=chaine70,).grid(row=3, column=1)
chaine72 = StringVar()
chaine72.set("NumLivre")
entree72 = Entry(fenetre7, textvariable=chaine72,).grid(row=3, column=2)
bouton70 = Button(fenetre7,image=image31,command=ajouter_emprunt).grid(row=3, column=3)
label72= Label(fenetre7, text="",width=10).grid(row=2,column=4)
label72= Label(fenetre7, text="Ajouter un emprunt").grid(row=1,column=2)
bouton72 = Button(fenetre7,image=image21,height=50,width=50,command=menu).grid(row=3, column=5)
label74 = Label(fenetre7, text="Menu").grid(row=4, column=5)
################################################################################
fenetre8 = Frame(root)
nomsup=StringVar()
prenomsup=StringVar()
adressesup=StringVar()
telephonesup=StringVar()
fixesupadh=StringVar()
def supprimer_adherent():
    identifiant='"'+str(get_id())+'"'
    x81=curseur.execute("select nomAdherent from adherent where identifiant="+str(identifiant))
    y81= x81.fetchone()
    x82=curseur.execute("select prenomAdherent from adherent where identifiant="+str(identifiant))
    y82= x82.fetchone()
    x83=curseur.execute("select adresse from adherent where identifiant="+str(identifiant))
    y83= x83.fetchone()
    x84=curseur.execute("select telephone from adherent where identifiant="+str(identifiant))
    y84= x84.fetchone()
    nomsup.set("Nom : "+str(y81[0]))
    prenomsup.set("Prenom : "+str(y82[0]))
    adressesup.set("adresse : "+str(y83[0]))
    telephonesup.set("telephone : "+str(y84[0]))
    fixesupadh.set("Adhérent Supprimé")
    Label82= Label(fenetre8,textvariable=fixesupadh).grid(row=5,column=2)
    Label83= Label(fenetre8,textvariable=nomsup).grid(row=6,column=1)
    Label84= Label(fenetre8,textvariable=prenomsup).grid(row=6,column=2)
    Label85= Label(fenetre8,textvariable=adressesup).grid(row=6,column=3)
    Label86= Label(fenetre8,textvariable=telephonesup).grid(row=6,column=4)
    requete="delete from adherent where identifiant =:identifiant"
    curseur.execute(requete,{"identifiant":identifiant[1:-1]})
    connexion.commit()
def resetsupadh():
    nomsup.set('')
    prenomsup.set('')
    adressesup.set('')
    telephonesup.set('')
    fixesupadh.set('')
chaine80 = StringVar()
chaine80.set("Identifiant")
entree = Entry(fenetre8, textvariable=chaine80, width=30).grid(row=2, column=1)
bouton80 = Button(fenetre8,image=image31,command=supprimer_adherent).grid(row=2, column=2)
bouton82 = Button(fenetre8,image=image21,height=50,width=50,command=menu).grid(row=2, column=4)
label84 = Label(fenetre8, text="Menu").grid(row=3, column=4)
Label80 = Label(fenetre8,text="Supprimer un adhérent").grid(row=1,column=1)
Label81 = Label(fenetre8,text="",width=10).grid(row=2,column=3)

################################################################################
fenetre9 = Frame(root)
idlivresup=StringVar()
nomlivresup=StringVar()
auteursup=StringVar()
editeursup=StringVar()
fixesupliv=StringVar()
def supprimer_livre():
    #'[4, 81, 6, 52]'
    isbn='"'+str(get_id())+'"'
    x91=curseur.execute("select idlivre from livre where idlivre="+isbn)
    y91= x91.fetchone()
    x92=curseur.execute("select titre from livre where idlivre="+isbn)
    y92= x92.fetchone()
    x93=curseur.execute("select auteur from livre where idlivre="+isbn)
    y93= x93.fetchone()
    x94=curseur.execute("select editeur from livre where idlivre="+isbn)
    y94= x94.fetchone()
    idlivresup.set("Numéro du livre : "+str(y91[0]))
    nomlivresup.set("titre du Livre: "+str(y92[0]))
    auteursup.set("Auteur : "+str(y93[0]))
    editeursup.set("Editeur : "+str(y94[0]))
    fixesupliv.set("Livre Supprimé")
    Label92= Label(fenetre9,textvariable=fixesupliv).grid(row=5,column=2)
    Label92= Label(fenetre9,textvariable=idlivresup).grid(row=6,column=1)
    Label92= Label(fenetre9,textvariable=nomlivresup).grid(row=6,column=2)
    Label92= Label(fenetre9,textvariable=auteursup).grid(row=6,column=3)
    Label92= Label(fenetre9,textvariable=editeursup).grid(row=6,column=4)
    requete="delete from livre where idlivre =:isbn"
    curseur.execute(requete,{"isbn":isbn[1:-1]})
    connexion.commit()
def resetsupliv():
    idlivresup.set('')
    nomlivresup.set('')
    auteursup.set('')
    editeursup.set('')
    fixesupliv.set('')
chaine90 = StringVar()
chaine90.set("IdLivre")
entree = Entry(fenetre9, textvariable=chaine90, width=30).grid(row=2, column=1)
bouton90 = Button(fenetre9,image=image31,command=supprimer_livre).grid(row=2, column=2)
bouton92 = Button(fenetre9,image=image21,height=50,width=50,command=menu).grid(row=2, column=4)
label94 = Label(fenetre9, text="Menu").grid(row=3, column=4)
Label90 = Label(fenetre9,text="Supprimer un livre").grid(row=1,column=1)
Label91 = Label(fenetre9,text="",width=10).grid(row=2,column=3)
################################################################################
fenetre10 = Frame(root)
idlivreempsup= StringVar()
nomlivreempsup= StringVar()
idadhempsup= StringVar()
nomadhempsup= StringVar()
fixeempsup=StringVar()
def supprimer_emprunt():
    isbn='"'+str(get_id())+'"'
    x101=curseur.execute("select NumEmprunt from emprunt where NumLivre="+isbn)
    y101= x101.fetchone()
    x102=curseur.execute("select NomLivre from emprunt where NumLivre="+isbn)
    y102= x102.fetchone()
    x103=curseur.execute("select Identifiant from emprunt where NumLivre="+isbn)
    y103= x103.fetchone()
    x104=curseur.execute("select NomAdherent from emprunt where NumLivre="+isbn)
    y104= x104.fetchone()
    idlivreempsup.set("Numéro du livre : "+str(isbn[1:-1]))
    nomlivreempsup.set("titre du Livre: "+str(y102[0]))
    idadhempsup.set("Identifiant de l'adhérent: "+str(y103[0]))
    nomadhempsup.set("Nom de l'adhérent: "+str(y104[0]))
    fixeempsup.set("Livre Rendu")
    Label102= Label(fenetre10,textvariable=fixeempsup).grid(row=5,column=2)
    Label102= Label(fenetre10,textvariable=idlivreempsup).grid(row=6,column=1)
    Label102= Label(fenetre10,textvariable=nomlivreempsup).grid(row=6,column=2)
    Label102= Label(fenetre10,textvariable=idadhempsup).grid(row=6,column=3)
    Label102= Label(fenetre10,textvariable=nomadhempsup).grid(row=6,column=4)
    requete="delete from emprunt where NumLivre =:isbn"
    curseur.execute(requete,{"isbn":isbn[1:-1]})
    connexion.commit()
def resetsupemp():
    idlivreempsup.set('')
    nomlivreempsup.set('')
    idadhempsup.set('')
    nomadhempsup.set('')
    fixeempsup.set('')
chaine100 = StringVar()
chaine100.set("NumEmprunt")
entree100 = Entry(fenetre10, textvariable=chaine100, width=30).grid(row=3, column=1)
bouton100 = Button(fenetre10,image=image31,command=supprimer_emprunt).grid(row=3, column=2)
bouton102 = Button(fenetre10,image=image21,height=50,width=50,command=menu).grid(row=3, column=4)
label104 = Label(fenetre10, text="Menu").grid(row=4, column=4)
Label100 = Label(fenetre10,text="Effectuer en retour").grid(row=1,column=1)
Label101 = Label(fenetre10,text="",width=10).grid(row=2,column=3)
################################################################################
fenetre1=Frame(root)
fenetre1.pack()
def affichagelisteadherent():
    fenetre1.pack_forget()
    fenetre2.pack()
    clearlisteadh()
def affichagelisteemprunt():
    fenetre1.pack_forget()
    fenetre3.pack()
    clearlisteemprunt()
def affichagelistelivre():
    fenetre1.pack_forget()
    fenetre4.pack()
    clearlistelivre()
def affichageaddlivre():
    fenetre1.pack_forget()
    fenetre6.pack()
    resetaddliv()
def affichageaddadherent():
    fenetre1.pack_forget()
    fenetre.pack()
    resetaddadh()
def affichagelisteretard():
    fenetre1.pack_forget()
    fenetre5.pack()
    clearlisteretard()
def affichageaddemprunt():
    fenetre1.pack_forget()
    fenetre7.pack()
    resetaddemp()
def affichagesupplivre():
    fenetre1.pack_forget()
    fenetre9.pack()
    resetsupliv()
def affichagesuppadh():
    fenetre1.pack_forget()
    fenetre8.pack()
    resetsupadh()
def affichagesuppempr():
    fenetre1.pack_forget()
    fenetre10.pack()
    resetsupemp()
def affichertri():
    fenetre1.pack_forget()
    frametri.pack()
    resettri()
def quitter():
    fenetre1.pack_forget()
    connexion.commit()
    connexion.close()
    exit()
label73 = Label(fenetre1, text="Gestionnaire de bibliotèque").grid(row=1, column=3)
label75 = Label(fenetre1, text="").grid(row=2,column=1)
label71 = Label(fenetre1, text="").grid(row=5,column=1)
label72 = Label(fenetre1, text="").grid(row=8,column=1)
image2 = ImageTk.PhotoImage(Image.open('annexe\icon.png').resize((50, 50)))
button2 = Button(fenetre1,image=image2,height=50,width=50,command=affichagelisteadherent).grid(row=3,column=1)
label2 = Label(fenetre1, text="Liste Adhérents",width=20).grid(row=4,column=1)
image3 = ImageTk.PhotoImage(Image.open('annexe\iconlivre2.jfif').resize((50, 50)))
button3 = Button(fenetre1,image=image3,height=50,width=50,command=affichagelistelivre).grid(row=3,column=2)
label3 = Label(fenetre1, text="Liste Livres",width=20).grid(row=4,column=2)
image5 = ImageTk.PhotoImage(Image.open('annexe\livrepero.jfif').resize((50, 50)))
button5 = Button(fenetre1,image=image5,height=50,width=50,command=affichagelisteemprunt).grid(row=3,column=3)
label5 = Label(fenetre1, text="Livres empruntés",width=20).grid(row=4,column=3)
image4 = ImageTk.PhotoImage(Image.open('annexe\iconaddlivre.jfif').resize((50, 50)))
button4 = Button(fenetre1,image=image4,height=50,width=50,command=affichageaddlivre).grid(row=6,column=2)
label4 = Label(fenetre1, text="Ajouter un livre",width=20).grid(row=7,column=2)
image6 = ImageTk.PhotoImage(Image.open('annexe\iconaddadh.jfif').resize((50, 50)))
button6 = Button(fenetre1,image=image6,height=50,width=50,command=affichageaddadherent).grid(row=6,column=1)
label6 = Label(fenetre1, text="Ajouter un adhérent",width=20).grid(row=7,column=1)
image7 = ImageTk.PhotoImage(Image.open('annexe\+emprutnlivre.png').resize((50, 50)))
button7 = Button(fenetre1,image=image7,height=50,width=50,command=affichageaddemprunt).grid(row=6,column=3)
label7 = Label(fenetre1, text="Ajouter un emprunt",width=20).grid(row=7,column=3)
image8 = ImageTk.PhotoImage(Image.open('annexe\iconretard.jfif').resize((50, 50)))
button8 = Button(fenetre1,image=image8,height=50,width=50,command=affichagelisteretard).grid(row=3,column=4)
label8 = Label(fenetre1, text="Liste retard",width=20).grid(row=4,column=4)
image9 = ImageTk.PhotoImage(Image.open('annexe\iconsupplivre.png').resize((50, 50)))
button9 = Button(fenetre1,image=image9,height=50,width=50,command=affichagesupplivre).grid(row=9,column=2)
label9 = Label(fenetre1, text="Supprimer un livre",width=20).grid(row=10,column=2)
image10 = ImageTk.PhotoImage(Image.open('annexe\iconsuppadh.jfif').resize((50, 50)))
button10 = Button(fenetre1,image=image10,height=50,width=50,command=affichagesuppadh).grid(row=9,column=1)
label10 = Label(fenetre1, text="Supprimer un adhérent",width=20).grid(row=10,column=1)
image11 = ImageTk.PhotoImage(Image.open('annexe\iconretourlivre.png').resize((50, 50)))
button11 = Button(fenetre1,image=image11,height=50,width=50,command=affichagesuppempr).grid(row=6,column=4)
label11 = Label(fenetre1, text="Éffectuer un retour",width=20).grid(row=7,column=4)
image12 = ImageTk.PhotoImage(Image.open('annexe\iconquitter.jfif').resize((50, 50)))
button12 = Button(fenetre1,image=image12,height=50,width=50,command=quitter).grid(row=3,column=5)
label12 = Label(fenetre1, text="Quitter",width=20).grid(row=4,column=5)
buttontri2 = Button(fenetre1, text="tri",command=affichertri).grid(row=9,column=7)
root.mainloop()