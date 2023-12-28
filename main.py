import random as r

import turtle
#### DEBUG --- Anciennes fonction ayant une qlq utilité + Fct debug

#fonction qui affiche le jeu
def AfficheJeu(jeu):
    print("| ", end="")

    for i in jeu:
        print(i, end=" | ")

    print("",end="\n")

