import subprocess
import time

#fontion affichage

def affichage(grille):
    print("   1 2 3")
    for i in range(len(grille)):
        print(LIGNES[i],"|",end="")
        for j in range(len(grille[i])):
            print(PIONS[grille[i][j]], end="|")
        print("")
    print("")

#fonction pour savoir si coord dans la grille

def est_dans_grille(coord, grille):
    return 0 <= ord(coord[0])-65 < len(grille) and 0 <= int(coord[1])-1 < len(grille)

#fonction pour savoir si coord valide

def coord_valide(coord):
    return len(coord) == 2 and 65 <= int(ord(coord[0])) <= 90 and 0 <= int(coord[1])-1 <= 9

#fonction pour savoir si il y a un pion sur la case de la grille

def case_valide(coord, grille):
    return grille[ord(coord[0])-65][int(coord[1])-1] == 0

#fonction pour savoir si le jeu est fini

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
            return 1
    if alligne_diag_droite == 3:
        if premier_pion_diag_droite == 1:
            print("Joueur 1 a gagné")
            return 1
        if premier_pion_diag_droite == 2:
            print("Joueur 2 a gagné")
            return 1
    
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
                return 1
        if alligne_ligne == 3:
            if premier_pion_ligne == 1:
                print("Joueur 1 a gagné")
                return 1
            if premier_pion_ligne == 2:
                print("Joueur 2 a gagné")
                return 1

    #cas d'égalité, personne gagne
    case_vide = 0
    for i in range(len(grille)):
        for k in range(len(grille[i])):
            if grille[i][k] == 0:
                case_vide += 1
    if case_vide == 0:
        print("Aucun gagnant, la partie est terminé")
        return 1

#fonction pour poser un pion

def poser_pion(grille, joueur, coord):
    grille[coord[0]][coord[1]] = joueur
    return grille

#fonction saisie

def saisie(grille):
    coord_brut = input("Veuillez saisir la coordonnée (format LETTRE CHIFFRE ex : A2) : ")
    i = 0
    while(i == 0):
        if(coord_valide(coord_brut) and est_dans_grille(coord_brut, grille) and case_valide(coord_brut, grille)):
            coord = ord(coord_brut[0])-65, int(coord_brut[1])-1
            i = 1
            print("coordonnée correct\n")
            return coord
        else:
            coord_brut = input("Coordonnée invalide veuillez resaisir : ")

#nom du jeu en fonction pour affichage

def morpion():
    print("---------")
    print("|MORPION|")
    print("---------")

#grille

grille = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#dico

LIGNES = {0:"A", 1:"B", 2:"C"}
PIONS = {0:" ", 1:"X", 2:"O"}

#lancement jeu

morpion()
joueur = 1
affichage(grille)
i = 0
while(i == 0):
    print("-----------------------------")
    print("| C'est au tour du joueur", joueur,"|")
    print("-----------------------------\n")
    coord = saisie(grille)
    grille = poser_pion(grille, joueur, coord)
    subprocess.call('cls', shell=True)
    morpion()
    affichage(grille)
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1
    if jeu_fini(grille, joueur) == 1:
        time.sleep(3)
        i = 1