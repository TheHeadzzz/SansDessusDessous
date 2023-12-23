def ConvertirEnSuite(nb):
    return [i for i in range(nb)]

def creerjeu(n, l):
    #n le nombre de cases
    #l la ligne du pion
    
    #on dermine ombien il y aura de pion par ligne
    Pion_par_ligne = [n//l for i in range(n//l)]
    #si le nombre de pions n'est pas un multiple de la ligne
    # on reparti les pions restants dans les lignes 
    if n%l != 0:
        for i in range(n%l):
            Pion_par_ligne[l-1-i] = Pion_par_ligne[l-1-i] + 1
    #On crée la liste du jeu
    jeu = []
    for pion in Pion_par_ligne:
        jeu.append(["R" for i in range(pion)])

    return jeu

def SelectionnerPion(ligne,pion,jeu,recto):
    #verifications que pour niv1 et 2 
    #on check pour etre sur qu'on a pas mit une ligne ou un pion qui n'existe pas
    #on compte les lignes et les pions de 1 a n
    if pion <= 0 or ligne <= 0:
        return "Probleme","Negatif"
    elif len(jeu) < ligne:
        return "Probleme","Ligne"
    
    elif len(jeu[ligne-1]) < pion:
        return "Probleme","Pion"
    pion -= 1
    ligne -= 1
    #Les tests sont passés on continue
    #on regarde si la carte est recto ou verso
    if jeu[ligne][pion] == "R": #carte recto
        jeu[ligne][pion] = "V"
        return jeu 
    else: #carte verso
        print("ok") 
        if recto == True: #si on ne peut que selectionner une carte recto renvoi une erreur
            print("ok2")
            return "Probleme","Recto"
        jeu[ligne][pion] = "R"
        return jeu 


