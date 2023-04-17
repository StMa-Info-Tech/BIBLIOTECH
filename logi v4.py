from tkinter import *
from customtkinter import *
from PIL import Image

root = Tk()
root.geometry("1070x870") #1920x1332
root.title("Bibliotech")
root.configure(bg='#0A1437')
Outfit = ('Outfit', 10)
OutfitBold = ('Outfit', 15,"bold")
OutfitTitle = ('Outfit', 30,"bold")
for i in range(25):
    Lab = CTkLabel(root, text="",corner_radius=10,height=10,width=10,font=Outfit,fg_color="#0A1437").grid(row=i,column=i)
def affichage_menu():
    LabelEspace_M0 = CTkLabel(root, text="",corner_radius=10,height=10,width=20,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=0,column=0)
    LabelTitre = CTkLabel(root, text="BIBLIOTECH",corner_radius=10,height= 19,width=120,font=OutfitTitle,text_color="white",fg_color="#0A1437").grid(row=2,column=1)
    LabelEspace_M1 = CTkLabel(root, text="",corner_radius=10,height=10,width=216,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=2,column=2)
    LabelTriple = CTkLabel(root, text="",corner_radius=33,height= 55,width=285,font=Outfit,text_color="white",fg_color="white").grid(row=1,rowspan=3,column=3,columnspan=3)
    LabelAdherent = CTkLabel(root, text="ADHERENT",corner_radius=20,height= 35,width=92,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white").grid(row=2,column=3,sticky="e")
    LabelLivre = CTkLabel(root, text="LIVRE",corner_radius=20,height= 35,width=61,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white").grid(row=2,column=4)
    LabelEmprunt = CTkLabel(root, text="EMPRUNT",corner_radius=20,height= 35,width=79,font=Outfit,text_color="#1C1C1E",fg_color="white",bg_color="white").grid(row=2,column=5,sticky="w")
    LabelEspace_M2 = CTkLabel(root, text="",corner_radius=10,height=10,width=230,font=Outfit,text_color="#1C1C1E",fg_color="#0A1437").grid(row=1,column=6,columnspan=2)
    LabelQuitter = CTkLabel(root, text="QUITTER",corner_radius=20,height= 50,width=87,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB").grid(row=1,rowspan=3,column=8,columnspan=2)
def affichage_liste_adherent():
    global num_liste_affiche
    global num_liste_max
    LabelAdherent = CTkLabel(root, text="ADHERENT",corner_radius=20,height= 35,width=92,font=Outfit,text_color="#1C1C1E",fg_color="#BAC8EB",bg_color="white").grid(row=2,column=3,sticky="e")
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
        for i in range(10):
            LabelNomAdherentI=CTkLabel(root,wraplength=180, text=Liste_Adherent_Affiche[i][1] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=1,sticky="w",padx=(25,0))
            LabelPrenomAdherentI=CTkLabel(root,wraplength=180, text=Liste_Adherent_Affiche[i][2] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=2,sticky="w",padx=(10,0))
            LabelAdresseAdherentI=CTkLabel(root,wraplength=180, text=Liste_Adherent_Affiche[i][3] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=3,columnspan=2,sticky="w",padx=(10,0))
            LabelTelephoneAdherentI=CTkLabel(root,wraplength=180, text=Liste_Adherent_Affiche[i][4] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=5,columnspan=2,sticky="w",padx=(10,0))
            LabelIdentifiantAdherentI=CTkLabel(root,wraplength=180, text=Liste_Adherent_Affiche[i][0] ,text_color="#1C1C1E",fg_color="white",bg_color="white",height=40,font=Outfit).grid(row=15+2*i,column=7,columnspan=2,sticky="w",padx=(10,0))
            LabelPoubelle= CTkButton(root,bg_color="white",fg_color="white",hover_color="red",text="",image=Image_Poubelle,width=15,height=15,command=test).grid(row=15+2*i,column=7,columnspan=3,sticky="e",padx=(0,20))
            if i!=9:
                progressbar = CTkProgressBar(root,height=1,width=1040,fg_color="#E6E6E6",progress_color="#E6E6E6",border_width=0).grid(row=16+2*i, column=1,columnspan=10)
    if num_liste_affiche>1:
        Label_Previous_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Previous_Page,width=15,height=15,command=Previous_Page).grid(row=13,column=8)
    if num_liste_affiche+1<=num_liste_max:
        Label_Next_Page = CTkButton(root,bg_color="white",fg_color="white",text="",image=Image_Next_Page,width=15,height=15,command=Next_Page).grid(row=13,column=9,sticky="w")

Liste_Adherent=[('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000')]
global Liste_Adherent_Affiche
Liste_Adherent_Affiche=[('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945'), ('4', 'TOPIAC', 'GERALDINE', '1 RUE DU CHILI', '0231789864'), ('6', 'DURAND', 'CELIA', '4 RUE DU COQUELICOT', '0523897845'), ('7', 'FRARIN', 'ISABELLE', '7 RUE DU TAILLEUR DE PIERRE', '0689784556'), ('[35, 74, 178, 127]', 'agnès', 'lemetais', '8 avenue croix guérin - caen', '00000000'),('1', 'DURAND', 'GILBERT', '4 RUE DU COQUELICOT', '0523897845'), ('2', 'DUPONT', 'FERNAND', '2 BIS PLACE FOCH', '0595685465'), ('3', 'MARTIN', 'JEAN', '5 BOULEVARD VEGAN', '0689788945')]
Image_Poubelle = CTkImage(Image.open("Annexe\Delete.png"),size=(15,15))
Image_Next_Page = CTkImage(Image.open("Annexe\Bold\Arrow - Right Circle.png"),size=(15,15))
Image_Previous_Page = CTkImage(Image.open("Annexe\Bold\Arrow - Left Circle.png"),size=(15,15))
global num_liste_affiche
global num_liste_max
num_liste_affiche=1
num_liste_max=None
def clear_frame():
    for label in root.winfo_children():
        label.destroy()
    for i in range(25):
        Lab = CTkLabel(root, text="",corner_radius=10,height=10,width=10,font=Outfit,fg_color="#0A1437").grid(row=i,column=i)
def test():
    print("test")
def Previous_Page():
    global num_liste_affiche
    global num_liste_max
    global Liste_Adherent_Affiche
    num_liste_affiche-=1
    num_liste_max=2
    Liste_Adherent_Affiche=[]
    for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
        Liste_Adherent_Affiche.append(Liste_Adherent[i])
    clear_frame()
    affichage_menu()
    affichage_liste_adherent()
def Next_Page():
    global num_liste_affiche
    global num_liste_max
    global Liste_Adherent_Affiche
    num_liste_affiche+=1
    num_liste_max=3
    if num_liste_affiche<num_liste_max:
        Liste_Adherent_Affiche=[]
        for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+11):
            print(i)
            Liste_Adherent_Affiche.append(Liste_Adherent[i])
    else:
        Liste_Adherent_Affiche=[]
        max= len(Liste_Adherent)%10
        print(max)
        for i in range((num_liste_affiche-1)*10,(num_liste_affiche-1)*10+max+1):
            print(i)
            Liste_Adherent_Affiche.append(Liste_Adherent[i])
    clear_frame()
    affichage_menu()
    affichage_liste_adherent()
affichage_menu()
affichage_liste_adherent()


root.mainloop()