from tkinter import *
from customtkinter import *
from PIL import Image

root = Tk()
root.geometry("1070x870") #1920x1332
root.title("Bibliotech")
root.configure(bg='#0A1437')
Outfit = ('Outfit', 10)
OutfitPlus = ('Outfit',15)
OutfitBold = ('Outfit', 15,"bold")
OutfitTitle = ('Outfit', 30,"bold")
for i in range(25):
    Lab = CTkLabel(root, text="",corner_radius=10,height=10,width=10,font=Outfit,fg_color="#0A1437").grid(row=i,column=i)
def affichage_menu():
    LabelEspace_M0 = CTkLabel(root, text="",corner_radius=10,height=10,width=20,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=0,column=0)
    LabelTitre = CTkLabel(root, text="BIBLIOTECH",corner_radius=10,height= 19,width=120,font=OutfitTitle,text_color="white",fg_color="#0A1437").grid(row=2,column=1)
    LabelEspace_M1 = CTkLabel(root, text="",corner_radius=10,height=10,width=216,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=2,column=2)
    LabelTriple = CTkLabel(root, text="",corner_radius=33,height= 55,width=285,font=Outfit,text_color="white",fg_color="white").grid(row=1,rowspan=3,column=3,columnspan=3)
    BouttonAdherent = CTkButton(root, text="ADHERENT",corner_radius=20,height= 35,width=92,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white",hover=False,command=ChangementAdherent).grid(row=2,column=3,sticky="e")
    BouttonLivre = CTkButton(root, text="LIVRE",corner_radius=20,height= 35,width=61,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white",hover=False,command=ChangementLivre).grid(row=2,column=4)
    BouttonEmprunt = CTkLabel(root, text="EMPRUNT",corner_radius=20,height= 35,width=79,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white").grid(row=2,column=5,sticky="w")
    LabelEspace_M2 = CTkLabel(root, text="",corner_radius=10,height=10,width=230,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=1,column=6,columnspan=2)
    LabelQuitter = CTkLabel(root, text="QUITTER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB").grid(row=1,rowspan=3,column=8,columnspan=2)
def affichage_liste_adherent():
    global num_liste_affiche
    global num_liste_max
    global page
    page="adherent"
    BouttonAdherent = CTkButton(root, text="ADHERENT",corner_radius=20,height= 35,width=92,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=ChangementAdherent).grid(row=2,column=3,sticky="e")
    LabelEspace_LA0 = CTkLabel(root, text="",corner_radius=10,height=30,font=Outfit,fg_color="#0A1437").grid(row=4,column=0)
    LabelQuintuple = CTkLabel(root, text="",corner_radius=15,height= 70,width=1025,font=Outfit,text_color="white",fg_color="white").grid(row=5,rowspan=3,column=1,columnspan=10)
    EntryNom = CTkEntry(root, placeholder_text="Nom",placeholder_text_color="#7882A5",width=180,corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0).grid(row=6,column=1,padx=(20,0))
    EntryPrenom = CTkEntry(root, placeholder_text="Prenom",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0).grid(row=6,column=2)
    EntryAdresse = CTkEntry(root, placeholder_text="Adresse",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0).grid(row=6,column=3,columnspan=2)
    EntryTelephone = CTkEntry(root, placeholder_text="Telephone",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0).grid(row=6,column=5,columnspan=2,padx=(20,0))
    BouttonAjouter = CTkLabel(root, text="AJOUTER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white").grid(row=6,column=8,columnspan=2)
    LabelSimple = CTkLabel(root, text="",corner_radius=15,height= 70,width=600,font=Outfit,text_color="white",fg_color="white").grid(row=9,rowspan=3,column=1,columnspan=4)
    EntryRecherche = CTkEntry(root, placeholder_text="Rechercher un Adherent",placeholder_text_color="#7882A5",corner_radius=10,height= 50,width=380,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0).grid(row=10,column=1,columnspan=2)
    LabelRecherche=CTkLabel(root, text="RECHERCHER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white").grid(row=10,column=3,columnspan=2,sticky="e",padx=(0,20))
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
    LabelNom = CTkLabel(root, text="Nom >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=1,pady=10,sticky="w",padx=(25,0))
    LabelPrenom = CTkLabel(root, text="Prenom >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=2,pady=10,sticky="w",padx=(10,0))
    LabelAdresse = CTkLabel(root, text="Adresse >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=3,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelTelephone = CTkLabel(root, text="Telephone >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=5,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelIdentifiant = CTkLabel(root, text="Identifiant >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=7,columnspan=2,pady=10,sticky="w",padx=(10,0))
    progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=14, column=1,columnspan=10)
    if len(Liste_Adherent)<=10:
        num_liste_max=1
        for i in range(len(Liste_Adherent)):
            LabelNomAdherentI=CTkLabel(root, text=Liste_Adherent[i][1] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=14+2*i,column=1)
            if i!=len(Liste_Adherent)-1:
                progressbar = CTkProgressBar(root,height=3,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=15+2*i, column=1,columnspan=10)

    else:
        num_liste_max=len(Liste_Adherent)//10
        if len(Liste_Adherent)%10!=0:
            num_liste_max+=1
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
            LabelAdresseAdherent=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][3] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="w",padx=(10,0))
            LabelTelephoneAdherent=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][4] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="w",padx=(10,0))
            LabelIdentifiantAdherent=CTkLabel(root,wraplength=180, text=Liste_Affiche[i][0] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="w",padx=(10,0))
            LabelPoubelle= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Poubelle,width=15,height=15,command=lambda row=i,page=num_liste_affiche: delete(row,page)).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=max-1:
                progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)
    if num_liste_affiche>1:
        Label_Previous_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Previous_Page,width=15,height=15,hover_color="#BAC8EB",command=Previous_Page).grid(row=13,column=8)
    if num_liste_affiche+1<=num_liste_max:
        Label_Next_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Next_Page,width=15,height=15,hover_color="#BAC8EB",command=Next_Page).grid(row=13,column=9,sticky="w")
def affichage_liste_livre():
    global num_liste_affiche
    global num_liste_max
    global page
    page="livre"
    BouttonLivre = CTkButton(root, text="LIVRE",corner_radius=20,height= 35,width=61,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white",hover=False,command=ChangementLivre).grid(row=2,column=4)
    LabelEspace_LL0 = CTkLabel(root, text="",corner_radius=10,height=30,font=Outfit,fg_color="#0A1437").grid(row=4,column=0)
    LabelQuintuple = CTkLabel(root, text="",corner_radius=15,height= 70,width=715,font=Outfit,text_color="white",fg_color="white").grid(row=5,rowspan=3,column=1,columnspan=5,sticky="w")
    EntryScan = CTkEntry(root, placeholder_text="Scannez le code barre d'un livre",placeholder_text_color="#7882A5",width=400,corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0).grid(row=6,column=1,columnspan=2,sticky="w",padx=(10,0))
    EntryCategorie = CTkEntry(root, placeholder_text="Catégorie",placeholder_text_color="#7882A5",corner_radius=10,height= 50,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",width=180,border_width=0).grid(row=6,column=2,columnspan=3,padx=(0,15),sticky="e")
    BouttonAjouter = CTkLabel(root, text="AJOUTER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white").grid(row=6,column=5,padx=(0,20),sticky="w")
    LabelSimple = CTkLabel(root, text="",corner_radius=15,height= 70,width=600,font=Outfit,text_color="white",fg_color="white").grid(row=9,rowspan=3,column=1,columnspan=4,padx=(0,20))
    EntryRecherche = CTkEntry(root, placeholder_text="Rechercher un livre",placeholder_text_color="#7882A5",corner_radius=10,height= 50,width=380,font=Outfit,text_color="#1C1C1E",fg_color="#E5EAF8",bg_color="white",border_width=0).grid(row=10,column=1,columnspan=2,sticky="w",padx=(10,0))
    LabelRecherche=CTkLabel(root, text="RECHERCHER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white").grid(row=10,column=3,columnspan=2,sticky="e",padx=(0,30))
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
    LabelISBN = CTkLabel(root, text="ISBN >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=1,pady=10,sticky="w",padx=(15,0))
    LabelTitre = CTkLabel(root, text="Titre >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=1,columnspan=2,padx=(100,0),sticky="w")
    LabelAuteur = CTkLabel(root, text="Auteur >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=3,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelEditeur = CTkLabel(root, text="Editeur >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=5,columnspan=2,pady=10,sticky="w",padx=(10,0))
    LabelCategorie = CTkLabel(root, text="Categorie >", text_color="#1C1C1E",fg_color="white",bg_color="white",font=OutfitBold).grid(row=13,column=7,columnspan=2,pady=10,sticky="w",padx=(10,0))
    progressbar = CTkProgressBar(root,height=1,width=1060,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=14, column=1,columnspan=10)

    if len(Liste_Livre)<=10:
        num_liste_max=1
        for i in range(len(Liste_Livre)):
            LabelNomLivreI=CTkLabel(root, text=Liste_Livre[i][1] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=14+2*i,column=1)
            if i!=len(Liste_Livre)-1:
                progressbar = CTkProgressBar(root,height=3,width=1060,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=15+2*i, column=1,columnspan=10)

    else:
        num_liste_max=len(Liste_Livre)//10
        if len(Liste_Livre)%10!=0:
            num_liste_max+=1
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
        Label_Previous_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Previous_Page,width=15,height=15,hover_color="#BAC8EB",command=Previous_Page).grid(row=13,column=8,sticky="w")
    if num_liste_affiche+1<=num_liste_max:
        Label_Next_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Next_Page,width=15,height=15,hover_color="#BAC8EB",command=Next_Page).grid(row=13,column=8,sticky="e")
Liste_Adherent=[('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'),('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'),('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'),('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'),('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'),('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556')]
Liste_Livre= [('9782212679847', 'Les réseaux informatiques par la pratique', 'Julien Launay','Eyrolles', '[4, 84, 208, 18, 20, 111, 129]', None, 'education'),('9782409024177', 'Django - Développez vos applications web en Python (fonctionnalités essentielles et bonnes pratiques)', 'Patrick Samson', '', '[4, 171, 209, 18, 20, 111, 128]', None, 'education'), ('9782340042100', 'Apprendre la programmation par le jeu - Découvrir Pygame avec de nouveaux jeux en Python', 'Vincent Maille', '', '[4, 80, 208, 18, 20, 111, 129]', None, 'education'), ('9782212673791', 'Programmer avec MySQL - SQL, transactions, PHP, Java, optimisations', 'Christian Soutou', 'Editions Eyrolles', '[4, 76, 208, 18, 20, 111, 129]', None, 'education'), ('9782412037461', 'Programmer avec MicroPython - Programmation Python de systèmes embarqués à microcontrôleurs', 'Nicholas H. Tollervey', 'First Interactive', '[4, 73, 209, 18, 20, 111, 129]', None, 'education'), ('9782017866305', "Numérique et Sciences Informatiques 1re Spécialité - Livre de l'élève", "Benoit Groz', 'Emmanuel Waller'", 'HACHETTE EDUC', '[4, 64, 209, 18, 20, 111, 129]', None, 'education'), ('9782017866343', 'Numérique et Sciences Informatiques - Tle Spécialité', "Céline Chevalier', 'Gilles Grimaud'", '', '[4, 60, 209, 18, 20, 111, 129]', None, 'education'), ('9781073887620', 'Dark Python - Apprenez à Créer Vos Propres Outils de Hacking (2e édition)', 'B. Anass', '', '[4, 56, 209, 18, 20, 111, 129]', None, 'education'), ('9782340038158', 'Spécialité numérique et sciences informatiques Tle', "Jean-Christophe Bonnefoy', 'Bertrand Petit", '', '[4, 52, 209, 18, 20, 111, 129]', None, 'education'), ('9782340031722', 'Spécialité numérique et sciences informatiques 1re', 'Serge Bays', '', '[4, 135, 209, 18, 20, 111, 128]', None, 'education'), ('9782203242227', 'Circus Maximus - La course de ma vie', 'Annelise Gray', '', '[4, 139, 209, 18, 20, 111, 128]', None, 'histoire'), ('9782824619675', 'Enquête étrusque au Louvre', 'Carole Declercq', '', '[4, 77, 207, 18, 20, 111, 129]', None, 'policier'),('9782212679847', 'Les réseaux informatiques par la pratique', 'Julien Launay','Eyrolles', '[4, 84, 208, 18, 20, 111, 129]', None, 'education'),('9782409024177', 'Django - Développez vos applications web en Python (fonctionnalités essentielles et bonnes pratiques)', 'Patrick Samson', '', '[4, 171, 209, 18, 20, 111, 128]', None, 'education'), ('9782340042100', 'Apprendre la programmation par le jeu - Découvrir Pygame avec de nouveaux jeux en Python', 'Vincent Maille', '', '[4, 80, 208, 18, 20, 111, 129]', None, 'education'), ('9782212673791', 'Programmer avec MySQL - SQL, transactions, PHP, Java, optimisations', 'Christian Soutou', 'Editions Eyrolles', '[4, 76, 208, 18, 20, 111, 129]', None, 'education'), ('9782412037461', 'Programmer avec MicroPython - Programmation Python de systèmes embarqués à microcontrôleurs', 'Nicholas H. Tollervey', 'First Interactive', '[4, 73, 209, 18, 20, 111, 129]', None, 'education'), ('9782017866305', "Numérique et Sciences Informatiques 1re Spécialité - Livre de l'élève", "Benoit Groz', 'Emmanuel Waller'", 'HACHETTE EDUC', '[4, 64, 209, 18, 20, 111, 129]', None, 'education'), ('9782017866343', 'Numérique et Sciences Informatiques - Tle Spécialité', "Céline Chevalier', 'Gilles Grimaud'", '', '[4, 60, 209, 18, 20, 111, 129]', None, 'education'), ('9781073887620', 'Dark Python - Apprenez à Créer Vos Propres Outils de Hacking (2e édition)', 'B. Anass', '', '[4, 56, 209, 18, 20, 111, 129]', None, 'education'), ('9782340038158', 'Spécialité numérique et sciences informatiques Tle', "Jean-Christophe Bonnefoy', 'Bertrand Petit", '', '[4, 52, 209, 18, 20, 111, 129]', None, 'education'), ('9782340031722', 'Spécialité numérique et sciences informatiques 1re', 'Serge Bays', '', '[4, 135, 209, 18, 20, 111, 128]', None, 'education'), ('9782203242227', 'Circus Maximus - La course de ma vie', 'Annelise Gray', '', '[4, 139, 209, 18, 20, 111, 128]', None, 'histoire'), ('9782824619675', 'Enquête étrusque au Louvre', 'Carole Declercq', '', '[4, 77, 207, 18, 20, 111, 129]', None, 'policier')]
global Liste_Livre_Affiche
Liste_Affiche = [('9782212679847', 'Les réseaux informatiques par la pratique', 'Julien Launay','Eyrolles', '[4, 84, 208, 18, 20, 111, 129]', None, 'education'),('9782409024177', 'Django - Développez vos applications web en Python (fonctionnalités essentielles et bonnes pratiques)', 'Patrick Samson', '', '[4, 171, 209, 18, 20, 111, 128]', None, 'education'), ('9782340042100', 'Apprendre la programmation par le jeu - Découvrir Pygame avec de nouveaux jeux en Python', 'Vincent Maille', '', '[4, 80, 208, 18, 20, 111, 129]', None, 'education'), ('9782212673791', 'Programmer avec MySQL - SQL, transactions, PHP, Java, optimisations', 'Christian Soutou', 'Editions Eyrolles', '[4, 76, 208, 18, 20, 111, 129]', None, 'education'), ('9782412037461', 'Programmer avec MicroPython - Programmation Python de systèmes embarqués à microcontrôleurs', 'Nicholas H. Tollervey', 'First Interactive', '[4, 73, 209, 18, 20, 111, 129]', None, 'education'), ('9782017866305', "Numérique et Sciences Informatiques 1re Spécialité - Livre de l'élève", "Benoit Groz', 'Emmanuel Waller'", 'HACHETTE EDUC', '[4, 64, 209, 18, 20, 111, 129]', None, 'education'), ('9782017866343', 'Numérique et Sciences Informatiques - Tle Spécialité', "Céline Chevalier', 'Gilles Grimaud'", '', '[4, 60, 209, 18, 20, 111, 129]', None, 'education'), ('9781073887620', 'Dark Python - Apprenez à Créer Vos Propres Outils de Hacking (2e édition)', 'B. Anass', '', '[4, 56, 209, 18, 20, 111, 129]', None, 'education'), ('9782340038158', 'Spécialité numérique et sciences informatiques Tle', "Jean-Christophe Bonnefoy', 'Bertrand Petit", '', '[4, 52, 209, 18, 20, 111, 129]', None, 'education'), ('9782340031722', 'Spécialité numérique et sciences informatiques 1re', 'Serge Bays', '', '[4, 135, 209, 18, 20, 111, 128]', None, 'education')]
Image_Poubelle = CTkImage(Image.open("Annexe\Delete.png"),size=(15,15))
Image_Next_Page = CTkImage(Image.open("Annexe\Bold\Arrow - Right Circle.png"),size=(15,15))
Image_Previous_Page = CTkImage(Image.open("Annexe\Bold\Arrow - Left Circle.png"),size=(15,15))
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
    global Liste_Affiche
    global num_liste_affiche
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
    global Liste_Affiche
    global num_liste_affiche
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
def delete(row,page_affiche):
    print(row,page_affiche)
def Previous_Page():
    global num_liste_affiche
    global num_liste_max
    global Liste_Adherent_Affiche
    global Liste_Livre_Affiche
    num_liste_affiche+=-1
    if page=="adherent":
        Liste_Adherent_Affiche=[]
        for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
            Liste_Adherent_Affiche.append(Liste_Adherent[i])
        clear_frame()
        affichage_menu()
        affichage_liste_adherent()
    elif page=="livre":
        Liste_Livre_Affiche=[]
        for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
            Liste_Livre_Affiche.append(Liste_Livre[i])
        clear_frame()
        affichage_menu()
        affichage_liste_livre()
def Next_Page():
    global num_liste_affiche
    global num_liste_max
    global Liste_Adherent_Affiche
    global Liste_Livre_Affiche
    num_liste_affiche+=1
    if page=="adherent":
        if num_liste_affiche<num_liste_max:
            Liste_Adherent_Affiche=[]
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
                Liste_Adherent_Affiche.append(Liste_Adherent[i])
        else:
            Liste_Adherent_Affiche=[]
            max= len(Liste_Adherent)%10
            if max==0:
                max=10
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+max):
                Liste_Adherent_Affiche.append(Liste_Adherent[i])
        clear_frame()
        affichage_menu()
        affichage_liste_adherent()
    elif page=="livre":
        if num_liste_affiche<num_liste_max:
            Liste_Livre_Affiche=[]
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
                Liste_Livre_Affiche.append(Liste_Livre[i])
        else:
            Liste_Livre_Affiche=[]
            max= len(Liste_Livre)%10
            if max==0:
                max=10
            for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+max):
                Liste_Livre_Affiche.append(Liste_Livre[i])
        clear_frame()
        affichage_menu()
        affichage_liste_livre()
def Lim(texte,nbmaxi):
    DicoCarMax = {1:65,2:30,3:30,4:20}
    NbCarMax=DicoCarMax[nbmaxi]
    if len(texte)>NbCarMax:
        return(str(texte[:NbCarMax])+"...")
    else:
        return(str(texte))
affichage_menu()
affichage_liste_livre()

root.mainloop()