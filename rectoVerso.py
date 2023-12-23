#GROUPE 1 : Alexandre BOURAEDA Raphaël GOURE   Rendu Séance 1
import random as r


#fonction qui crée le jeu
def creerjeu(n):
    jeu = []
    for i in range(n):
        jeu.append("V")
    return jeu


#fonction qui retourne un pion choisi
def SelectionnerPion(pion,jeu,verso):
    #on regarde si la carte est recto ou verso
    if jeu[pion] == "V": #carte verso
        jeu[pion] = "R"
        return jeu 

    else: #carte recto
        if verso == True: #si on ne peut que selectionner une carte recto renvoi une erreur
            return "Probleme_Verso"

        jeu[pion] = "V"
        return jeu


#fonction qui verifie si un joueur a gagné
def CheckWin(jeu):     
    #Return True si il n'y a plus de Verso et donc que le joueur a gagné
    for pion in jeu:

        if pion == "V":
            return False

    return True


#fonction qui affiche le jeu
def AfficheJeu(jeu):
    print("| ", end="")

    for i in jeu:
        print(i, end=" | ")

    print("",end="\n")


#fonction qui fait jouer l'ordinateur
def ordinateur(jeu, NbPions):
    print("c'est le tour de l'ordinateur : ", end ="")
    
    tour=r.randint(1,2)

    #fait rejouer l'ordinateur tant qu'il n'a pas choisi une carte verso
    condition = "Probleme_Verso"
    while condition == "Probleme_Verso":
        choix=r.randint(0,NbPions-1)
        condition= SelectionnerPion(choix, jeu, True)
    
     #Dans la fonction on compte de 0 a n or le joueur vois les pions numérotés de 1 a n+1
     #on fait donc choix +1 pour que le joueur vois les bonnes valeurs
    print(f"Il joue le pion {choix + 1}")
    jeu = condition
    
    #si tour = 2 l'ordinateur rejoue
    if tour == 2 and choix != 1:
        print("l'ordinateur joue une deuxieme fois ! Il retourne le pion : ", end ="")
        choix=r.randint(0,choix-1) #selection un nombre entre le pion 1 et le pion inferieur a choix
        print(choix + 1)
        jeu = SelectionnerPion(choix,jeu,False)
        

    return jeu


#fonction regroupant les action pour faire jouer le joueur
def joueur (jeu, choix, recto,choix_precedent,NbPions):
    for number in choix:
        if not 48<=ord(number)<=57: 
            return "Probleme_Entier"
            
    choix = int(choix)
    if choix_precedent <= choix:
        return "Probleme_Choix"
    
    if choix > NbPions or -choix >=0: #on verifie que le choix n'est pas trop grand ni negatif ni egal a 0
        return "Probleme_Index"

    jeu = SelectionnerPion(choix-1, jeu, recto)
    
    if jeu == "Probleme_Verso":
        return "Probleme_Verso"
    
    return jeu


jouer = True
NbPions = r.randint(5,12)
jeu = creerjeu(NbPions)
while jouer:
    
    #on fait jouer le joueur
    AfficheJeu(jeu)
    tour_joueur = True
    Verso = True
    choix_precedent=NbPions+1# On le met a cette valeur pour ne pas avoir de probleme pendant le premier tour du joueur
    while tour_joueur:
        
        #on fait joueur le joueur

        choix = input(f"Quel carte veux-tu retourner ? (1,..,{NbPions})")

        #verso = True => obligé de retourner V
        #verso = False => on a voulu rejouer on peut tout retourner
        action = joueur(jeu,choix,Verso,choix_precedent,NbPions)
        if action == "Probleme_Entier":
            print("Choisi un nombre entier")
        elif action == "Probleme_Verso":#si c'est le cas le J a choisi une carte R au lieu d'une carte V
            print("Tu dois choisir une carte Verso !!!!!")
        elif action == "Probleme_Choix":
            print("Tu es obligé de choisir une carte de plus petite valeur")
        elif action == "Probleme_Index":
            print(f"tu dois choisir une carte entre 1 et {NbPions}")
        
        #si le choix est "correct" on continue
        else:
            choix = int(choix)
            jeu = action #On met a jour le jeu de carte
            tour_joueur = False
            #on verifie si le joueur a gagné
            if CheckWin(jeu) == True:
                AfficheJeu(jeu)
                print("BRAVO VOUS AVEZ GAGNE !!!!")
                jouer = False

            #si verso = False alors le joueur a deja rejoué
            elif Verso != False:
                
                #si ce n'est pas le cas on demande s'il veut rejouer
                if  choix != 1 and input("Veux tu rejouer (o/n)") == "o":
                    choix_precedent = choix
                    AfficheJeu(jeu)
                    Verso = False
                    tour_joueur = True
            

    #si jouer = False le joueur a gagné on demande au J s'il veut recommencer une partie 
    if jouer != False:
    #le joueur n'a pas gagné c'est au tour de l'ordinateur
        AfficheJeu(jeu)
        jeu = ordinateur(jeu, NbPions)
        
        if CheckWin(jeu) == True:
            AfficheJeu(jeu)
            print("L'ordinateur a gagné !!! ")
            jouer = False