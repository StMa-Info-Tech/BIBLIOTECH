from sqlite3 import *

def afficher_menu():
    print("1  Créer la table livre")
    print("2  Créer la table adherent")
    print("3  créer la table emprunt")
    print("4  Ajouter un livre")
    print("5  Ajouter un adhérent")
    print("6  Ajouter un emprunt")
    print("7  Afficher la liste des livres")
    print("8  Afficher la liste des livres empruntés")
    print("9  Afficher la liste des adhérents")
    print("10 Afficher la liste des emprunts en retard")
    print("11 Supprimer un livre")
    print("12 Supprimer un adhérent")
    print("13 Retour de livre")
    print("14 Supprimer toute la base de données")
    print("0  Quitter")
def lire_action():
    afficher_menu()
    reponse = int(input("Votre choix : "))
    choix=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    while reponse not in choix:
        afficher_menu()
        reponse = int(input("Votre choix : "))
    return reponse
def table_livre():
    requete="CREATE TABLE if not exists livre(isbn varchar(10) primary key not null,titre varchar(255) not null,auteur varchar(40) not null,editeur varchar(40) not nulL,unique(isbn))"
    resultat = curseur.execute(requete)
def table_adherent():
    requete="CREATE TABLE if not exists adherent (identifiant integer primary key autoincrement,nomAdherent varchar(255),prenomAdherent varchar(255),adresse varchar(255),telephone varchar(10),unique(identifiant),unique(nomAdherent,prenomAdherent))"
    resultat = curseur.execute(requete)
def table_emprunt():
    requete="CREATE TABLE if not exists emprunt(isbn varchar (10),identifiant	INTEGER,dateemprunt date,dateretour date,FOREIGN KEY(identifiant) REFERENCES adherent(identifiant),PRIMARY KEY(isbn,identifiant),FOREIGN KEY(isbn) REFERENCES livre(isbn),unique(isbn,identifiant))"
    resultat = curseur.execute(requete)
def ajouter_adherent():
    pass

def liste_adherent():
    pass
def ajouter_livre():
    pass
def ajouter_emprunt():
    pass
def supprimer_adherent():
    identifiant=int(input("identification de l'adhérent à supprimer "))
    requete="delete from adherent where identifiant =:identifiant"
    curseur.execute(requete,{"identifiant":identifiant})
def supprimer_livre():
    isbn=input("isbn du livre à supprimer ?")
    requete="delete from livre where isbn =:isbn"
    curseur.execute(requete,{"isbn":isbn})
def supprimer_emprunt():
    isbn=input("isbn du livre emprunté ?")
    requete="delete from emprunt where isbn =:isbn"
    curseur.execute(requete,{"isbn":isbn})
def supprimer_tables():
    pass
def liste_emprunt():
    pass
def liste_livre():
    pass
def liste_retard():
    pass
def rechercher_adherent(nom):
    curseur.execute("select identifiant from adherent where nomadherent=:nom", {"nom": nom})
    a=curseur.fetchone()
    return a[0]
def appli():
    termine = False
    while not(termine):
        action = lire_action()
        if action == 0:
            termine = True
        else:
            table_actions[action]()
            connexion.commit()

table_actions = [None,table_livre,table_adherent,table_emprunt,ajouter_livre,ajouter_adherent,ajouter_emprunt,liste_livre,liste_emprunt,liste_adherent,liste_retard,supprimer_livre,supprimer_adherent,supprimer_emprunt,supprimer_tables]

connexion = connect('bibliotheque.db')
aujourdhui=input("Date aujourd'hui sous la forme JJ/MM/AAAA ?") # à éliminer, trouver la date en utilisant la bibliothèque time
curseur = connexion.cursor()
appli()
curseur.execute("select * from adherent")

connexion.close()
