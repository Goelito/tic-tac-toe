import tkinter.font as font
from tkinter import *

# modele grille
#
#     1 2 3
#  A | | | |
#  B | | | |
#  C | | | |

#variable global

global grille
global joueur
joueur = 1
grille = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#fonction pour changer de couleur au survol de la souris

def a1survol_bouton(event):
    a1['bg'] = "grey85"
    
def a1sortie_survol_bouton(event):
    a1['bg'] = "whitesmoke"
    
def a2survol_bouton(event):
    a2['bg'] = "grey85"
    
def a2sortie_survol_bouton(event):
    a2['bg'] = "whitesmoke"
    
def a3survol_bouton(event):
    a3['bg'] = "grey85"
    
def a3sortie_survol_bouton(event):
    a3['bg'] = "whitesmoke"
    
def b1survol_bouton(event):
    b1['bg'] = "grey85"
    
def b1sortie_survol_bouton(event):
    b1['bg'] = "whitesmoke"
    
def b2survol_bouton(event):
    b2['bg'] = "grey85"
    
def b2sortie_survol_bouton(event):
    b2['bg'] = "whitesmoke"
    
def b3survol_bouton(event):
    b3['bg'] = "grey85"
    
def b3sortie_survol_bouton(event):
    b3['bg'] = "whitesmoke"
    
def c1survol_bouton(event):
    c1['bg'] = "grey85"
    
def c1sortie_survol_bouton(event):
    c1['bg'] = "whitesmoke"
    
def c2survol_bouton(event):
    c2['bg'] = "grey85"
    
def c2sortie_survol_bouton(event):
    c2['bg'] = "whitesmoke"
    
def c3survol_bouton(event):
    c3['bg'] = "grey85"
    
def c3sortie_survol_bouton(event):
    c3['bg'] = "whitesmoke"

#fonction pour placer des pions par case
def clique_a1():
    if a1["text"] == "   ":
        if joueur == 1:
            a1["text"] = "X"
            grille[0][0] = 1
        else:
            a1["text"] = "O"
            grille[0][0] = 2
        tk_joueur()
        finito(joueur)
    
def clique_a2():
    if a2["text"] == "   ":
        if joueur == 1:
            a2["text"] = "X"
            grille[0][1] = 1
        else:
            a2["text"] = "O"
            grille[0][1] = 2
        tk_joueur()
        finito(joueur)
    
def clique_a3():
    if a3["text"] == "   ":
        if joueur == 1:
            a3["text"] = "X"
            grille[0][2] = 1
        else:
            a3["text"] = "O"
            grille[0][2] = 2
        tk_joueur()
        finito(joueur)
    
def clique_b1():
    if b1["text"] == "   ":
        if joueur == 1:
            b1["text"] = "X"
            grille[1][0] = 1
        else:
            b1["text"] = "O"
            grille[1][0] = 2
        tk_joueur()
        finito(joueur)
    
def clique_b2():
    if b2["text"] == "   ":
        if joueur == 1:
            b2["text"] = "X"
            grille[1][1] = 1
        else:
            b2["text"] = "O"
            grille[1][1] = 2
        tk_joueur()
        finito(joueur)
    
def clique_b3():
    if b3["text"] == "   ":
        if joueur == 1:
            b3["text"] = "X"
            grille[1][2] = 1
        else:
            b3["text"] = "O"
            grille[1][2] = 2
        tk_joueur()
        finito(joueur)
    
def clique_c1():
    if c1["text"] == "   ":
        if joueur == 1:
            c1["text"] = "X"
            grille[2][0] = 1
        else:
            c1["text"] = "O"
            grille[2][0] = 2
        tk_joueur()
        finito(joueur)
    
def clique_c2():
    if c2["text"] == "   ":
        if joueur == 1:
            c2["text"] = "X"
            grille[2][1] = 1
        else:
            c2["text"] = "O"
            grille[2][1] = 2
        tk_joueur()
        finito(joueur)
    
def clique_c3():
    if c3["text"] == "   ":
        if joueur == 1:
            c3["text"] = "X"
            grille[2][2] = 1
        else:
            c3["text"] = "O"
            grille[2][2] = 2
        tk_joueur()
        finito(joueur)

#fonction affichage tour joueur

def tk_joueur():
    affichage(grille)
    global joueur
    print(joueur)
    if joueur == 2:
        label_tour_joueur["text"] = "C'est au tour du joueur 1"
        joueur = 1
    else:
        label_tour_joueur["text"] = "C'est au tour du joueur 2"
        joueur = 2

#fonction disabled bouton + ferme la fenetre

def fin():
    a1["state"] = DISABLED
    a2["state"] = DISABLED
    a3["state"] = DISABLED
    b1["state"] = DISABLED
    b2["state"] = DISABLED
    b3["state"] = DISABLED
    c1["state"] = DISABLED
    c2["state"] = DISABLED
    c3["state"] = DISABLED
    

#fonction pour terminer le jeu

def finito(joueur):
    resultat = jeu_fini(grille, joueur)
    if resultat == 0:
        label_fin_partie["text"] = "égalité"
        label_fin_partie.pack(side=BOTTOM)
        fin()
    if resultat == 1:
        label_fin_partie["text"] = "joueur 1 gagne"
        label_fin_partie.pack(side=BOTTOM)
        fin()
    if resultat == 2:
        label_fin_partie["text"] = "joueur 2 gagne"
        label_fin_partie.pack(side=BOTTOM)
        fin()
    
#tkinter init

fenetre = Tk()
fenetre.geometry("335x550")
fenetre.resizable(height=False, width=False)
fenetre.title("Tic tac Toe")
fenetre["bg"] = "grey90"

#affichage joueur

label_tour_joueur = Label(fenetre, text="C'est au tour du joueur 1")
label_tour_joueur["bg"] = "grey90"
label_tour_joueur["font"] = 25
label_tour_joueur.pack()

#affichage fin de partie

label_fin_partie = Label(fenetre, text="")
label_fin_partie["bg"] = "grey90"
label_fin_partie["font"] = 25
label_fin_partie.pack(side=BOTTOM)

#création de la grille et des boutons

grille_tk = Frame(fenetre, bg="white")

#creation des lignes

ligneA = Frame(grille_tk, bg="white")
ligneB = Frame(grille_tk, bg="white")
ligneC = Frame(grille_tk, bg="white")

#taille écriture bouton

f = font.Font(family="Dejavu Sans", size=57, weight="bold")


#création boutons

a1 = Button(ligneA, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_a1, width=2, height=1)
a2 = Button(ligneA, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_a2, width=2, height=1)
a3 = Button(ligneA, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_a3, width=2, height=1)
b1 = Button(ligneB, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_b1, width=2, height=1)
b2 = Button(ligneB, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_b2, width=2, height=1)
b3 = Button(ligneB, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_b3, width=2, height=1)
c1 = Button(ligneC, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_c1, width=2, height=1)
c2 = Button(ligneC, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_c2, width=2, height=1)
c3 = Button(ligneC, text="   ",bg="whitesmoke", relief=SUNKEN, activebackground="grey85", borderwidth=0, font=f, command=clique_c3, width=2, height=1)

#affichage grille

grille_tk.pack(expand=YES)

#affichage lignes

ligneA.grid(row=0, column=0)
ligneB.grid(row=1, column=0)
ligneC.grid(row=2, column=0)

#affichage boutons

liste_boutons = [
    [a1, a2, a3],
    [b1, b2, b3],
    [c1, c2, c3]
]

#changer de couleur les boutons au survol de la souris

a1.bind("<Enter>", a1survol_bouton)
a1.bind("<Leave>", a1sortie_survol_bouton)
a2.bind("<Enter>", a2survol_bouton)
a2.bind("<Leave>", a2sortie_survol_bouton)
a3.bind("<Enter>", a3survol_bouton)
a3.bind("<Leave>", a3sortie_survol_bouton)
b1.bind("<Enter>", b1survol_bouton)
b1.bind("<Leave>", b1sortie_survol_bouton)
b2.bind("<Enter>", b2survol_bouton)
b2.bind("<Leave>", b2sortie_survol_bouton)
b3.bind("<Enter>", b3survol_bouton)
b3.bind("<Leave>", b3sortie_survol_bouton)
c1.bind("<Enter>", c1survol_bouton)
c1.bind("<Leave>", c1sortie_survol_bouton)
c2.bind("<Enter>", c2survol_bouton)
c2.bind("<Leave>", c2sortie_survol_bouton)
c3.bind("<Enter>", c3survol_bouton)
c3.bind("<Leave>", c3sortie_survol_bouton)

for i in range(3):
    for j in range(3):
        liste_boutons[i][j].grid(row=0, column=j)

#fontion affichage (fonction debug)

def affichage(grille):
    for i in range(len(grille)):
        print("|",end="")
        for j in range(len(grille[i])):
            print(PIONS[grille[i][j]], end="|")
        print("")
    print("")

#fonction pour savoir si le jeu est fini (qui calcul sur grille)

def jeu_fini(grille, joueur):
    #savoir si 3 pions sont alligné en diagonnale et qui est le gagnant
    premier_pion_diag_gauche = grille[0][0]
    premier_pion_diag_droite = grille[0][2]
    alligne_diag_gauche = 0
    alligne_diag_droite = 0
    for p in range(len(grille)):
        if grille[p][p] == premier_pion_diag_gauche:
            alligne_diag_gauche += 1
        if grille[p][2-p] == premier_pion_diag_droite:
            alligne_diag_droite += 1
    if alligne_diag_gauche == 3:
        if premier_pion_diag_gauche == 1:
            print("Joueur 1 a gagné")
            return 1
        if premier_pion_diag_gauche == 2:
            print("Joueur 2 a gagné")
            return 2
    if alligne_diag_droite == 3:
        if premier_pion_diag_droite == 1:
            print("Joueur 1 a gagné")
            return 1
        if premier_pion_diag_droite == 2:
            print("Joueur 2 a gagné")
            return 2
    
    #savoir si 3 pions sont alligné (ligne, colonne) et qui est le gagnant
    for j in range(len(grille)):
        premier_pion_ligne = grille[j][0]
        premier_pion_colonne = grille[0][j]
        alligne_ligne = 0
        alligne_collone = 0
        for l in range(3):
            if grille[j][l] == premier_pion_ligne:
                alligne_ligne += 1
            if grille[l][j] == premier_pion_colonne:
                alligne_collone += 1 
        if alligne_collone == 3:
            if premier_pion_colonne == 1:
                print("Joueur 1 a gagné")
                return 1
            if premier_pion_colonne == 2:
                print("Joueur 2 a gagné")
                return 2
        if alligne_ligne == 3:
            if premier_pion_ligne == 1:
                print("Joueur 1 a gagné")
                return 1
            if premier_pion_ligne == 2:
                print("Joueur 2 a gagné")
                return 2

    #cas d'égalité, personne gagne
    case_vide = 0
    for i in range(len(grille)):
        for k in range(len(grille[i])):
            if grille[i][k] == 0:
                case_vide += 1
    if case_vide == 0:
        print("Aucun gagnant, la partie est terminé")
        return 0

#dico

PIONS = {0:" ", 1:"X", 2:"O"}

#lancement jeu

affichage(grille)

#a placer fin de code

fenetre.mainloop()
