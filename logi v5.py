import nfc
from tkinter import *
from customtkinter import *
from PIL import Image
from sqlite3 import *
from datetime import date, timedelta
from isbnlib import *

root = Tk()
root.geometry("1070x870") #1920x1332
root.title("Bibliotech")
root.configure(bg='#0A1437')
root.resizable(False, False)
Outfit = ('Outfit', 10)
OutfitPlus = ('Outfit',15)
OutfitBold = ('Outfit', 15,"bold")
OutfitTitle = ('Outfit', 30,"bold")
connexion = connect('bibliotheque.db')
today_date = date.today()
td = timedelta(30)
curseur = connexion.cursor()
for i in range(25):
    Lab = CTkLabel(root, text="",corner_radius=10,height=10,width=10,font=Outfit,fg_color="#0A1437").grid(row=i,column=i)
def affichage_menu():
    LabelEspace_M0 = CTkLabel(root, text="",corner_radius=10,height=10,width=20,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=0,column=0)
    LabelTitre = CTkLabel(root, text="BIBLIOTECH",corner_radius=10,height= 19,width=120,font=OutfitTitle,text_color="white",fg_color="#0A1437").grid(row=2,column=1)
    LabelEspace_M1 = CTkLabel(root, text="",corner_radius=10,height=10,width=216,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=2,column=2)
    LabelTriple = CTkLabel(root, text="",corner_radius=33,height= 55,width=285,font=Outfit,text_color="white",fg_color="white").grid(row=1,rowspan=3,column=3,columnspan=3)
    BouttonAdherent = CTkButton(root, text="ADHERENT",corner_radius=20,height= 35,width=92,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white",hover=False,command=ChangementAdherent).grid(row=2,column=3,sticky="e")
    BouttonLivre = CTkButton(root, text="LIVRE",corner_radius=20,height= 35,width=61,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white",hover=False,command=ChangementLivre).grid(row=2,column=4)
    BouttonEmprunt = CTkButton(root, text="EMPRUNT",corner_radius=20,height= 35,width=79,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white",hover=False,command=ChangementEmprunts).grid(row=2,column=5,sticky="w")
    LabelEspace_M2 = CTkLabel(root, text="",corner_radius=10,height=10,width=230,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=1,column=6,columnspan=2)
    BouttonQuitter = CTkButton(root, text="QUITTER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",hover=False,command=Quitter).grid(row=1,rowspan=3,column=8,columnspan=2)
def affichage_liste_adherent():
    global Liste_Adherent
    global num_liste_affiche
    global num_liste_max
    global page
    global EntryNom
    global EntryPrenom
    global EntryAdresse
    global EntryTelephone
    global EntryRechercheAdherent
    page="adherent"
    num_liste_max=len(Liste_Adherent)//10
    if len(Liste_Adherent)%10!=0:
        num_liste_max+=1
    BouttonAdherent = CTkButton(root, text="ADHERENT",corner_radius=20,height= 35,width=92,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=ChangementAdherent).grid(row=2,column=3,sticky="e")
    LabelEspace_LA0 = CTkLabel(root, text="",corner_radius=10,height=30,font=Outfit,fg_color="#0A1437").grid(row=4,column=0)
    LabelQuintuple = CTkLabel(root, text="",corner_radius=15,height= 70,width=1025,font=Outfit,text_color="white",fg_color="white").grid(row=5,rowspan=3,column=1,columnspan=10)
    EntryNom = CTkEntry(root, placeholder_text="Nom",placeholder_text_color="#7882A5",width=180,corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0)
    EntryNom.grid(row=6,column=1,padx=(20,0))
    EntryPrenom = CTkEntry(root, placeholder_text="Prenom",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0)
    EntryPrenom.grid(row=6,column=2)
    EntryAdresse = CTkEntry(root, placeholder_text="Adresse",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0)
    EntryAdresse.grid(row=6,column=3,columnspan=2)
    EntryTelephone = CTkEntry(root, placeholder_text="Telephone",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0)
    EntryTelephone.grid(row=6,column=5,columnspan=2,padx=(20,0))
    BouttonAjouter = CTkButton(root, text="AJOUTER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=Ajouter_Adherent).grid(row=6,column=8,columnspan=2)
    LabelSimple = CTkLabel(root, text="",corner_radius=15,height= 70,width=600,font=Outfit,text_color="white",fg_color="white").grid(row=9,rowspan=3,column=1,columnspan=4)
    EntryRechercheAdherent = CTkEntry(root, placeholder_text="Rechercher un Adherent",placeholder_text_color="#7882A5",corner_radius=10,height= 50,width=380,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0)
    EntryRechercheAdherent.grid(row=10,column=1,columnspan=2)
    BouttonRecherche=CTkButton(root, text="RECHERCHER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=RechercherAdherent).grid(row=10,column=3,columnspan=2,sticky="e",padx=(0,20))
    if len(Liste_Adherent)<=10:
        HauteurDeca=50+50*len(Liste_Adherent)
    else:
        if num_liste_affiche==num_liste_max:
            if len(Liste_Adherent)%10!=0:
                HauteurDeca=50+50*(len(Liste_Adherent)%10)
            else:
                HauteurDeca=600
        else:
            HauteurDeca=600
    LabelDeca = CTkLabel(root, text="",corner_radius=15,height= HauteurDeca,width=1025,font=Outfit,text_color="white",fg_color="white").grid(row=13,rowspan=22,column=1,columnspan=10,sticky="n")
    LabelNom = CTkButton(root, text="Nom >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="nomAdherent",table="adherent":sortby(column,table)).grid(row=13,column=1,pady=10,sticky="w",padx=(25,0))
    LabelPrenom = CTkButton(root, text="Prenom >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="prenomAdherent",table="adherent":sortby(column,table)).grid(row=13,column=2,pady=10,sticky="w",padx=(10,0))
    LabelAdresse = CTkButton(root, text="Adresse >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="adresse",table="adherent":sortby(column,table)).grid(row=13,column=3,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelTelephone = CTkButton(root, text="Telephone >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="telephone",table="adherent":sortby(column,table)).grid(row=13,column=5,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelIdentifiant = CTkButton(root, text="Identifiant >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="identifiant",table="adherent":sortby(column,table)).grid(row=13,column=7,columnspan=2,pady=10,sticky="w",padx=(10,0))
    progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=14, column=1,columnspan=10)
    if len(Liste_Adherent)<=10:
        for i in range(len(Liste_Adherent)):
            LabelNomAdherentI=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][1] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,sticky="w",padx=(25,0))
            LabelPrenomAdherent=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][2] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=2,sticky="w",padx=(10,0))
            LabelAdresseAdherent=CTkLabel(root,wraplength=180, text=Lim(Liste_Affiche[i][3],2) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="w",padx=(10,0))
            LabelTelephoneAdherent=CTkLabel(root,wraplength=180, text=Lim(Liste_Affiche[i][4],3) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="w",padx=(10,0))
            LabelIdentifiantAdherent=CTkLabel(root,wraplength=180, text=Lim(Liste_Affiche[i][0],4) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="w",padx=(10,0))
            LabelPoubelle= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Poubelle,width=15,height=15,command=lambda row=i,page=num_liste_affiche: delete(row,page)).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=len(Liste_Adherent)-1:
                progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)

    else:
        max=0
        if num_liste_affiche==num_liste_max:
            if len(Liste_Adherent)%10!=0:
                max=len(Liste_Adherent)%10
            else:
                max=10
        else:
            max=10
        for i in range(max):
            LabelNomAdherentI=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][1] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,sticky="w",padx=(25,0))
            LabelPrenomAdherent=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][2] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=2,sticky="w",padx=(10,0))
            LabelAdresseAdherent=CTkLabel(root,wraplength=180, text=Lim(Liste_Affiche[i][3],2) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="w",padx=(10,0))
            LabelTelephoneAdherent=CTkLabel(root,wraplength=180, text=Lim(Liste_Affiche[i][4],3) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="w",padx=(10,0))
            LabelIdentifiantAdherent=CTkLabel(root,wraplength=180, text=Lim(Liste_Affiche[i][0],4) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="w",padx=(10,0))
            LabelPoubelle= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Poubelle,width=15,height=15,command=lambda row=i,page=num_liste_affiche: delete(row,page)).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=max-1:
                progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)
    if num_liste_affiche>1:
        Label_Previous_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Previous_Page,width=15,height=15,hover_color="#BAC8EB",command=Previous_Page).grid(row=13,column=8)
    if num_liste_affiche+1<=num_liste_max:
        Label_Next_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Next_Page,width=15,height=15,hover_color="#BAC8EB",command=Next_Page).grid(row=13,column=9,sticky="w")
def affichage_liste_livre():
    global Liste_Affiche
    global num_liste_affiche
    global num_liste_max
    global page
    global EntryScanLivre
    global EntryCategorie
    global EntryRechercheLivre
    page="livre"
    num_liste_max=len(Liste_Livre)//10
    if len(Liste_Livre)%10!=0:
        num_liste_max+=1
    BouttonLivre = CTkButton(root, text="LIVRE",corner_radius=20,height= 35,width=61,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=ChangementLivre).grid(row=2,column=4)
    LabelEspace_LL0 = CTkLabel(root, text="",corner_radius=10,height=30,font=Outfit,fg_color="#0A1437").grid(row=4,column=0)
    LabelQuintuple = CTkLabel(root, text="",corner_radius=15,height= 70,width=715,font=Outfit,text_color="white",fg_color="white").grid(row=5,rowspan=3,column=1,columnspan=5,sticky="w")
    EntryScanLivre = CTkEntry(root, placeholder_text="Scannez le code barre d'un livre",placeholder_text_color="#7882A5",width=400,corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0)
    EntryScanLivre.grid(row=6,column=1,columnspan=2,sticky="w",padx=(10,0))
    EntryCategorie = CTkEntry(root, placeholder_text="Catégorie",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0)
    EntryCategorie.grid(row=6,column=2,columnspan=3,padx=(0,15),sticky="e")
    BouttonAjouter = CTkButton(root, text="AJOUTER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=Ajouter_Livre).grid(row=6,column=5,padx=(0,20),sticky="w")
    LabelSimple = CTkLabel(root, text="",corner_radius=15,height= 70,width=600,font=Outfit,text_color="white",fg_color="white").grid(row=9,rowspan=3,column=1,columnspan=4,padx=(0,20))
    EntryRechercheLivre = CTkEntry(root, placeholder_text="Rechercher un livre",placeholder_text_color="#7882A5",corner_radius=10,height= 50,width=380,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0)
    EntryRechercheLivre.grid(row=10,column=1,columnspan=2,sticky="w",padx=(10,0))
    BouttonRecherche=CTkButton(root, text="RECHERCHER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=RechercherLivre).grid(row=10,column=3,columnspan=2,sticky="e",padx=(0,30))
    if len(Liste_Livre)<=10:
        HauteurDeca=50+50*len(Liste_Livre)
    else:
        if num_liste_affiche==num_liste_max:
            if len(Liste_Livre)%10!=0:
                HauteurDeca=50+50*(len(Liste_Livre)%10)
            else:
                HauteurDeca=600
        else:
            HauteurDeca=600
    LabelDeca = CTkLabel(root, text="",corner_radius=15,height= HauteurDeca,width=1035,font=Outfit,text_color="white",fg_color="white").grid(row=13,rowspan=22,column=1,columnspan=10,sticky="n",padx=(0,25))
    LabelISBN = CTkButton(root, text="ISBN >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="isbn",table="livre":sortby(column,table)).grid(row=13,column=1,pady=10,sticky="w",padx=(0,0))
    LabelTitre = CTkButton(root, text="Titre >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="titre",table="livre":sortby(column,table)).grid(row=13,column=1,columnspan=2,padx=(100,0),sticky="w")
    LabelAuteur = CTkButton(root, text="Auteur >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="auteur",table="livre":sortby(column,table)).grid(row=13,column=3,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelEditeur = CTkButton(root, text="Editeur >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="editeur",table="livre":sortby(column,table)).grid(row=13,column=5,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelCategorie = CTkButton(root, text="Categorie >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="categorie",table="livre":sortby(column,table)).grid(row=13,column=7,columnspan=2,pady=10,sticky="w",padx=(10,0))
    progressbar = CTkProgressBar(root,height=1,width=1060,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=14, column=1,columnspan=10)

    if len(Liste_Livre)<=10:
        for i in range(len(Liste_Livre)):
            LabelISBNLivre=CTkLabel(root, text=Liste_Affiche[i][0] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,sticky="w",padx=(15,0))
            LabelTitreLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][1],1) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,columnspan=2,padx=(100,0),sticky="w")
            LabelAuteurLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][2],2) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="w",padx=(10,0))
            LabelEditeurLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][3],3) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="w",padx=(10,0))
            LabelCategorieLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][6],4) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="w",padx=(10,0))
            LabelPoubelle= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Poubelle,width=15,height=15,command=lambda row=i,page=num_liste_affiche: delete(row,page)).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=len(Liste_Livre)-1:
                progressbar = CTkProgressBar(root,height=1,width=1060,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)
    else:
        max=0
        if num_liste_affiche==num_liste_max:
            if len(Liste_Livre)%10!=0:
                max=len(Liste_Livre)%10
            else:
                max=10
        else:
            max=10
        for i in range(max):
            LabelISBNLivre=CTkLabel(root, text=Liste_Affiche[i][0] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,sticky="w",padx=(15,0))
            LabelTitreLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][1],1) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,columnspan=2,padx=(100,0),sticky="w")
            LabelAuteurLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][2],2) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="w",padx=(10,0))
            LabelEditeurLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][3],3) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="w",padx=(10,0))
            LabelCategorieLivre=CTkLabel(root, text=Lim(Liste_Affiche[i][6],4) ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="w",padx=(10,0))
            LabelPoubelle= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Poubelle,width=15,height=15,command=lambda row=i,page=num_liste_affiche: delete(row,page)).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=max-1:
                progressbar = CTkProgressBar(root,height=1,width=1060,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)
    if num_liste_affiche>1:
        Label_Previous_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Previous_Page,width=15,height=15,hover_color="#BAC8EB",command=Previous_Page).grid(row=13,column=8,columnspan=2,sticky="w")
    if num_liste_affiche+1<=num_liste_max:
        Label_Next_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Next_Page,width=15,height=15,hover_color="#BAC8EB",command=Next_Page).grid(row=13,column=8,columnspan=2)
def affichage_liste_emprunts():
    global num_liste_affiche
    global num_liste_max
    global page
    global Livre_Emprunt
    global EntryScanEmprunt
    global EntryAdherentCarte
    if page!="emprunt" and page!="retard":
        page="emprunt"
    num_liste_max=len(Liste_Emprunt)//10
    if len(Liste_Emprunt)%10!=0:
        num_liste_max+=1
    BouttonEmprunt = CTkButton(root, text="EMPRUNT",corner_radius=20,height= 35,width=92,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=ChangementEmprunts).grid(row=2,column=5,sticky="w")
    LabelEspace_LA0 = CTkLabel(root, text="",corner_radius=10,height=30,font=Outfit,fg_color="#0A1437").grid(row=4,column=0)
    LabelQuintuple = CTkLabel(root, text="",corner_radius=15,height= 70,width=1025,font=Outfit,text_color="white",fg_color="white").grid(row=5,rowspan=3,column=1,columnspan=10,sticky="w")
    EntryScanEmprunt = CTkEntry(root, placeholder_text="Scannez le NFC d'un livre",placeholder_text_color="#7882A5",width=370,corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0)
    EntryScanEmprunt.grid(row=6,column=1,columnspan=3,padx=(10,0),sticky='w')
    EntryAdherentCarte = CTkEntry(root, placeholder_text="Scannez la carte de l'adhérent",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=370,border_width=0)
    EntryAdherentCarte.grid(row=6,column=2,columnspan=6,sticky='w',padx=(190,0))
    BouttonRetour = CTkButton(root, text="RETOUR",corner_radius=20,height= 50,width=110,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=Retour).grid(row=6,column=6,columnspan=4, padx=(0,130), sticky='e')
    BouttonAjouter = CTkButton(root, text="AJOUTER",corner_radius=20,height= 50,width=110,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=Emprunt).grid(row=6,column=7,columnspan=3, padx=(0,10),sticky="e")
    LabelButton = CTkButton(root, text="Livres en retard",corner_radius=15,height= 30,width=115,font=Outfit,text_color="#1C1C1E",fg_color="white",hover=False,command=Retard).grid(row=9,rowspan=3,column=7,columnspan=3,padx=(90,0))
    if len(Liste_Emprunt)<=10:
        HauteurDeca=50+50*len(Liste_Emprunt)
    else:
        if num_liste_affiche==num_liste_max:
            if len(Liste_Emprunt)%10!=0:
                HauteurDeca=50+50*(len(Liste_Emprunt)%10)
            else:
                HauteurDeca=650
        else:
            HauteurDeca=650
    LabelDeca = CTkLabel(root, text="",corner_radius=15,height= HauteurDeca,width=1025,font=Outfit,text_color="white",fg_color="white").grid(row=13,rowspan=22,column=1,columnspan=10,sticky="wn")
    Label_Livre_Emprunt = CTkButton(root, text="Livre >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="NomLivre",table=page:sortby(column,table)).grid(row=13,column=1,pady=10,sticky="w",padx=(25,0))
    Label_Auteur_Emprunt = CTkButton(root, text="Auteur >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="Auteur",table=page:sortby(column,table)).grid(row=13,column=2,pady=10,sticky="w",padx=(10,0))
    Label_Nom_Emprunt = CTkButton(root, text="Nom de l'Adhérent >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="NomAdherent",table=page:sortby(column,table)).grid(row=13,column=3,columnspan=2,pady=10,sticky="w",padx=(10,0))
    Label_Prenom_Emprunt = CTkButton(root, text="Prenom de l'Adhérent >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="PrenomAdherent",table=page:sortby(column,table)).grid(row=13,column=5,columnspan=2,pady=10,sticky="w",padx=(10,0))
    Label_Date_Emprunt = CTkButton(root, text="Retour >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold,hover=False,command=lambda column="DateRetour",table=page:sortby(column,table)).grid(row=13,column=7,columnspan=2,pady=10,sticky="w",padx=(10,0))
    progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=14, column=1,columnspan=10)
    if len(Liste_Emprunt)<=10:
        for i in range(len(Liste_Emprunt)):
            LabelLivre=CTkLabel(root,wraplength=180, text=Liste_Emprunt[i][1]  ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,sticky="nw",padx=(25,0))
            LabelAuteur=CTkLabel(root,wraplength=180, text=Liste_Emprunt[i][7] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=2,sticky="nw",padx=(10,0))
            LabelAdherent=CTkLabel(root,wraplength=180, text=Liste_Emprunt[i][6] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="nw",padx=(10,0))
            LabelRetour=CTkLabel(root,wraplength=180, text=Liste_Emprunt[i][8] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="nw",padx=(10,0))
            LabelIdentifiant=CTkLabel(root,wraplength=180, text=Liste_Emprunt[i][3] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="nw",padx=(10,0))
            if Liste_Emprunt[i][3]<=str(today_date):
                LabelRetard= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Retard,width=15,height=15,command=lambda row=i,page=num_liste_affiche: delete(row,page)).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=len(Liste_Emprunt)-1:
                progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)

    else:
        max=0
        if num_liste_affiche==num_liste_max:
            if len(Liste_Emprunt)%10!=0:
                max=len(Liste_Emprunt)%10
            else:
                max=10
        else:
            max=10
        for i in range(max):
            LabelLivre=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][1]  ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,sticky="w",padx=(25,0))
            LabelAuteur=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][2] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=2,sticky="w",padx=(10,0))
            LabelAdherent=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][3] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="w",padx=(10,0))
            LabelRetour=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][4] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="w",padx=(10,0))
            LabelIdentifiant=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][0] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="w",padx=(10,0))
            LabelRetard= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Retard,width=15,height=15,command=lambda row=i,page=num_liste_affiche: delete(row,page)).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=max-1:
                progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)
    if num_liste_affiche>1:
        Label_Previous_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Previous_Page,width=15,height=15,hover_color="#BAC8EB",command=Previous_Page).grid(row=13,column=8)
    if num_liste_affiche+1<=num_liste_max:
        Label_Next_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Next_Page,width=15,height=15,hover_color="#BAC8EB",command=Next_Page).grid(row=13,column=9,sticky="w")
global Liste_Livre_Affiche
Liste_Affiche = []
Image_Poubelle = CTkImage(Image.open("Annexe\Delete.png"),size=(15,15))
Image_Next_Page = CTkImage(Image.open("Annexe\Bold\Arrow - Right Circle.png"),size=(15,15))
Image_Previous_Page = CTkImage(Image.open("Annexe\Bold\Arrow - Left Circle.png"),size=(15,15))
Image_Retard = CTkImage(Image.open("Annexe\Retard.png"),size=(15,15))
global num_liste_affiche
global num_liste_max
num_liste_affiche=1
num_liste_max=None
global page
page=None
def clear_frame():
    for label in root.winfo_children():
        label.destroy()
    for i in range(25):
        Lab = CTkLabel(root, text="",corner_radius=10,height=10,width=10,font=Outfit,fg_color="#0A1437").grid(row=i,column=i)
def ChangementAdherent():
    global Liste_Adherent
    global Liste_Affiche
    global num_liste_affiche
    requete="SELECT * FROM adherent"
    curseur.execute(requete)
    connexion.commit()
    Liste_Adherent= curseur.fetchall()
    num_liste_affiche=1
    Liste_Affiche=[]
    if len(Liste_Adherent)<=10:
        max=len(Liste_Adherent)
    else:
        max=10
    for i in range(max):
        Liste_Affiche.append(Liste_Adherent[i])
    clear_frame()
    affichage_menu()
    affichage_liste_adherent()
def ChangementLivre():
    global Liste_Livre
    global Liste_Affiche
    global num_liste_affiche
    requete="SELECT * FROM livre"
    curseur.execute(requete)
    connexion.commit()
    Liste_Livre= curseur.fetchall()
    num_liste_affiche=1
    Liste_Affiche=[]
    if len(Liste_Livre)<=10:
        max=len(Liste_Livre)
    else:
        max=10
    for i in range(max):
        Liste_Affiche.append(Liste_Livre[i])
    clear_frame()
    affichage_menu()
    affichage_liste_livre()
def ChangementEmprunts():
    global Liste_Emprunt
    global Liste_Affiche
    global num_liste_affiche
    requete="SELECT * FROM emprunt"
    curseur.execute(requete)
    connexion.commit()
    Liste_Emprunt = curseur.fetchall()
    num_liste_affiche=1
    Liste_Affiche=[]
    if len(Liste_Emprunt)<=10:
        max=len(Liste_Emprunt)
    else:
        max=10
    for i in range(max):
        Liste_Affiche.append(Liste_Emprunt[i])
    clear_frame()
    affichage_menu()
    affichage_liste_emprunts()
def delete(row,page_affiche):
    global num_liste_affiche
    num_liste_affiche+=-1
    if page=="adherent":
        requete='DELETE FROM adherent WHERE identifiant="'+str(Liste_Adherent[(page_affiche-1)*10+row][0])+'"'
        curseur.execute(requete)
        connexion.commit()
        Liste_Adherent.pop((page_affiche-1)*10+row)
        Next_Page()
    elif page=="livre":
        requete='DELETE FROM livre WHERE idlivre="'+str(Liste_Livre[(page_affiche-1)*10+row][4])+'"'
        curseur.execute(requete)
        connexion.commit()
        Liste_Livre.pop((page_affiche-1)*10+row)
        Next_Page()
    else:
        pass
def Previous_Page():
    global num_liste_affiche
    global num_liste_max
    global Liste_Affiche
    global Liste_Livre
    global Liste_Adherent
    global Liste_Emprunt
    num_liste_affiche+=-1
    if page=="adherent":
        Liste_Affiche=[]
        for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
            Liste_Affiche.append(Liste_Adherent[i])
        clear_frame()
        affichage_menu()
        affichage_liste_adherent()
    elif page=="livre":
        Liste_Affiche=[]
        for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
            Liste_Affiche.append(Liste_Livre[i])
        clear_frame()
        affichage_menu()
        affichage_liste_livre()
    elif page=="emprunt" or page=="retard":
        Liste_Affiche=[]
        for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
            Liste_Affiche.append(Liste_Emprunt[i])
        clear_frame()
        affichage_menu()
        affichage_liste_emprunts()
def Next_Page():
    global num_liste_affiche
    global num_liste_max
    global Liste_Affiche
    global Liste_Livre
    global Liste_Adherent
    global Liste_Emprunt
    num_liste_affiche+=1
    if page=="adherent":
        num_liste_max=len(Liste_Adherent)//10
        if len(Liste_Adherent)%10!=0:
            num_liste_max+=1
        if num_liste_affiche<num_liste_max:
            Liste_Affiche=[]
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
                Liste_Affiche.append(Liste_Adherent[i])
        else:
            Liste_Affiche=[]
            max= len(Liste_Adherent)%10
            if max==0:
                max=10
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+max):
                Liste_Affiche.append(Liste_Adherent[i])
        clear_frame()
        affichage_menu()
        affichage_liste_adherent()
    elif page=="livre":
        num_liste_max=len(Liste_Livre)//10
        if len(Liste_Livre)%10!=0:
            num_liste_max+=1
        if num_liste_affiche<num_liste_max:
            Liste_Affiche=[]
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
                Liste_Affiche.append(Liste_Livre[i])
        else:
            Liste_Affiche=[]
            max= len(Liste_Livre)%10
            if max==0:
                max=10
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+max):
                Liste_Affiche.append(Liste_Livre[i])
        clear_frame()
        affichage_menu()
        affichage_liste_livre()
    elif page=="emprunt" or page=="retard":
        num_liste_max=len(Liste_Emprunt)//10
        if len(Liste_Emprunt)%10!=0:
            num_liste_max+=1
        if num_liste_affiche<num_liste_max:
            Liste_Affiche=[]
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
                Liste_Affiche.append(Liste_Emprunt[i])
        else:
            Liste_Affiche=[]
            max= len(Liste_Emprunt)%10
            if max==0:
                max=10
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+max):
                Liste_Affiche.append(Liste_Emprunt[i])
        clear_frame()
        affichage_menu()
        affichage_liste_emprunts()
def Lim(texte,nbmaxi):
    DicoCarMax = {1:65,2:30,3:30,4:20}
    NbCarMax=DicoCarMax[nbmaxi]
    if len(texte)>NbCarMax:
        return(str(texte[:NbCarMax])+"...")
    else:
        return(str(texte))

def sortby(column,table):
    global Liste_Livre
    global Liste_Adherent
    global Liste_Emprunt
    global num_liste_affiche
    num_liste_affiche+=-1
    if table!="retard":
        requete = f"SELECT * from {table} ORDER BY {column}"
        curseur.execute(requete)
        connexion.commit()
        affichage_menu()
        if table=="livre":
            Liste_Livre= curseur.fetchall()
            Next_Page()
        elif table=="adherent":
            Liste_Adherent= curseur.fetchall()
            Next_Page()
        else:
            Liste_Emprunt= curseur.fetchall()
            Next_Page()
    else:
        requete = f"SELECT * from emprunt WHERE DATE(DateRetour)<DATE('now') ORDER BY {column}"
        curseur.execute(requete)
        Liste_Emprunt= curseur.fetchall()
        Next_Page()
def Edit_Nb_Auteur(string):
    if string.count("'")>=4:
        n1=string.find("'")
        n2=string.find("'",n1)
        n3=string.find("'",n2)
        n4=string.find("'",n3)
        return string[:n4]
    else:
        return string
def Ajouter_Livre():
    global num_liste_affiche
    global Liste_Livre
    num_liste_affiche+=-1
    #idlivre= get_id()
    idlivre="1"
    categorie =EntryCategorie.get()
    isbn = EntryScanLivre.get()
    book=meta(isbn)
    auteur = str(book.get('Authors'))[2:-2]
    titre = str(book.get('Title'))
    editeur = str(book.get('Publisher'))
    requete='INSERT INTO livre(isbn,titre,auteur,editeur,idlivre,categorie) VALUES("'+str(isbn)+'","'+str(titre)+'","'+Edit_Nb_Auteur(str(auteur))+'","'+Edit_Nb_Auteur(str(editeur))+'","'+str(idlivre)+'","'+str(categorie)+'")'
    curseur.execute(requete)
    connexion.commit()
    curseur.execute("SELECT * FROM livre")
    Liste_Livre = curseur.fetchall()
    Next_Page()
def Ajouter_Adherent():
    global num_liste_affiche
    global Liste_Adherent
    num_liste_affiche+=-1
    #identifiant= get_id()
    identifiant = "10"
    nom = EntryNom.get()
    prenom = EntryPrenom.get()
    adresse = EntryAdresse.get()
    Telephone = EntryTelephone.get()
    requete='INSERT INTO adherent(identifiant,nomAdherent,prenomAdherent,adresse,telephone) VALUES("'+identifiant.upper()+'","'+nom.upper()+'","'+prenom.upper()+'","'+adresse.upper()+'","'+Telephone.upper() +'")'
    curseur.execute(requete)
    connexion.commit()
    curseur.execute("SELECT * FROM adherent")
    Liste_Adherent = curseur.fetchall()
    Next_Page()
def Emprunt():
    global Liste_Emprunt
    global num_liste_affiche
    Id_Livre = EntryScanEmprunt.get()
    Id_Adherent = EntryAdherentCarte.get()
    requeteLivre = f'SELECT * FROM livre WHERE idlivre="{Id_Livre}"'
    curseur.execute(requeteLivre)
    Data_Livre = curseur.fetchone()
    requeteAdherent = f'SELECT * FROM adherent WHERE identifiant="{Id_Adherent}"'
    curseur.execute(requeteAdherent)
    Data_Adherent = curseur.fetchone()
    print(f'Date Livre : {Data_Livre} \n Data Adherent : {Data_Adherent}')
    if Data_Livre==None or Data_Adherent == None:
        print('Information Incorrect')
    else:
        Id_Livre=Data_Livre[4]
        Nom_Livre=Data_Livre[1]
        Date=today_date
        Date_Retour=today_date+td
        Id_Adherent=Data_Adherent[0]
        Nom_Adherent=Data_Adherent[1]
        Prenom_Adherent=Data_Adherent[2]
        Auteurs=Data_Livre[2]
        requete=f'INSERT INTO emprunt(NumLivre,NomLivre,DateEmprunt,DateRetour,Identifiant,NomAdherent,PrenomAdherent,Auteur) values("{Id_Livre}","{Nom_Livre}","{Date}","{Date_Retour}","{Id_Adherent}","{Nom_Adherent}","{Prenom_Adherent}","{Auteurs}")'
        curseur.execute(requete)
        connexion.commit()
        curseur.execute("SELECT * FROM emprunt")
        Liste_Emprunt = curseur.fetchall()
        num_liste_affiche-=1
        Next_Page()
def Retour():
    global Liste_Emprunt
    global num_liste_affiche
    Id_Livre = EntryScanEmprunt.get()
    Id_Adherent = EntryAdherentCarte.get()
    requeteLivre = f'SELECT * FROM livre WHERE idlivre="{Id_Livre}"'
    curseur.execute(requeteLivre)
    Data_Livre = curseur.fetchone()
    requeteAdherent = f'SELECT * FROM adherent WHERE identifiant="{Id_Adherent}"'
    curseur.execute(requeteAdherent)
    Data_Adherent = curseur.fetchone()
    print(f'Date Livre : {Data_Livre} \n Data Adherent : {Data_Adherent}')
    if Data_Livre==None or Data_Adherent == None:
        print('Information Incorrect')
    else:
        requete=f'DELETE FROM emprunt WHERE NumLivre="{Id_Livre}" AND Identifiant="{Id_Adherent}"'
        curseur.execute(requete)
        connexion.commit()
        curseur.execute("SELECT * FROM emprunt")
        Liste_Emprunt = curseur.fetchall()
        num_liste_affiche-=1
        Next_Page()
def RechercherAdherent():
    global num_liste_affiche
    global Liste_Adherent
    DataRecherche = EntryRechercheAdherent.get()
    requete='SELECT * FROM adherent WHERE nomAdherent like "%'+str(DataRecherche)+'%" OR prenomAdherent like "%'+str(DataRecherche)+'%" OR adresse like "%'+str(DataRecherche)+'%" OR telephone like "%'+str(DataRecherche)+'%"'
    curseur.execute(requete)
    Liste_Adherent = curseur.fetchall()
    if Liste_Adherent!=[]:
        num_liste_affiche+=-1
        Next_Page()
    else:
        print('Aucun résultat !')
        requete= "SELECT * FROM adherent"
        curseur.execute(requete)
        Liste_Adherent = curseur.fetchall()
def RechercherLivre():
    global num_liste_affiche
    global Liste_Livre
    DataRecherche = EntryRechercheLivre.get()
    requete='SELECT * FROM livre WHERE isbn like "%'+str(DataRecherche)+'%" OR titre like "%'+str(DataRecherche)+'%" OR auteur like "%'+str(DataRecherche)+'%" OR idlivre like "%'+str(DataRecherche)+'%" OR editeur like "%'+str(DataRecherche)+'%"'
    curseur.execute(requete)
    Liste_Livre = curseur.fetchall()
    if Liste_Livre!=[]:
        num_liste_affiche+=-1
        Next_Page()
    else:
        print('Aucun résultat !')
        requete= "SELECT * FROM livre"
        curseur.execute(requete)
        Liste_Livre = curseur.fetchall()
def Retard():
    global page
    global Liste_Emprunt
    global num_liste_affiche
    if page=="emprunt":
        page="retard"
        curseur.execute("SELECT * FROM emprunt WHERE DATE(DateRetour)<DATE('now')")
        Liste_Emprunt = curseur.fetchall()
        num_liste_affiche-=1
        Next_Page()
    elif page=="retard":
        page="emprunt"
        curseur.execute("SELECT * FROM emprunt")
        Liste_Emprunt = curseur.fetchall()
        num_liste_affiche-=1
        Next_Page()

#def RechercherEmprunt():
#    DataRecherche = EntryRechercheEmprunt.get()
#    requete='SELECT * FROM emprunt WHERE numlivre like "%'+str(DataRecherche)+'%" OR nomlivre like "%'+str(DataRecherche)+'%" OR DateEmprunt like "%'+str(DataRecherche)+'%" OR NomAdherent like "%'+str(DataRecherche)+'%"OR Identifiant like "%'+str(DataRecherche)+'%" OR NumEmprunt like "%'+str(DataRecherche)+'%" OR DateRetour like "%'+str(DataRecherche)+'%"'

def Quitter():
    connexion.commit()
    connexion.close()
    exit()
ChangementLivre()

root.mainloop()