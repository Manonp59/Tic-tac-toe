grille = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]



def afficher_grille(g):
    for ligne in g :
        for elt in ligne:
            print ('|',elt,'|', end="")
        print("\n")
        
def jouer_coup_1(g):
    print("Joueur 1, c'est à toi.")
    ligne = input('Sur quelle ligne voulez-vous jouer ?')
    colonne = input('Sur quelle colonne voulez-vous jouer ?')
    while ligne not in [0,1,2,"0","1","2"] or colonne not in [0,1,2,"0","1","2"] :
        print('Saisir des coordonnées correctes.')
        ligne = input('Sur quelle ligne voulez-vous jouer ?')
        colonne = input('Sur quelle colonne voulez-vous jouer ?')
    while g[int(ligne)][int(colonne)] != " " :
        print('Cette case est déjà prise, merci de choisir une case vide.')
        ligne = input('Sur quelle ligne voulez-vous jouer ?')
        colonne = input('Sur quelle colonne voulez-vous jouer ?')
    if g[int(ligne)][int(colonne)] == " " :
        g[int(ligne)][int(colonne)] = 'X'

def jouer_coup_2(g):
    print("Joueur 2, c'est à toi.")
    ligne = input('Sur quelle ligne voulez-vous jouer ?')
    colonne = input('Sur quelle colonne voulez-vous jouer ?')
    while ligne not in [0,1,2,"0","1","2"] or colonne not in [0,1,2,"0","1","2"] :
        print('Saisir des coordonnées correctes.')
        ligne = input('Sur quelle ligne voulez-vous jouer ?')
        colonne = input('Sur quelle colonne voulez-vous jouer ?')
    while g[int(ligne)][int(colonne)] != " ":
        print('Cette case est déjà prise, merci de choisir une case vide.')
        ligne = input('Sur quelle ligne voulez-vous jouer ?')
        colonne = input('Sur quelle colonne voulez-vous jouer ?')
    if g[int(ligne)][int(colonne)] == " " :
        g[int(ligne)][int(colonne)] = 'O'
 
def est_gagnee(grille):
    for ligne in grille:
        if ligne[0]== ligne[1]== ligne[2] and ligne[0]!= " ":
            return True
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i]!= " ":
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0]!= " ":
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != " ":
        return True
    return False

    
def gagnant(grille):
    if grille[0][0] == grille[0][1] == grille[0][2] == 'X' or grille[1][0] == grille[1][1] == grille[1][2] == 'X' or grille[2][0] == grille[2][1] == grille[2][2] == 'X' or grille[0][0] == grille[1][0] == grille[2][0] == 'X' or grille[0][1] == grille[1][1] == grille[1][2] == 'X' or grille[0][2] == grille[1][2] == grille[2][2] == 'X' or grille[0][0] == grille[1][1] == grille[2][2] == 'X' or grille[0][2] == grille[1][1] == grille[2][0] == 'X':
         print('Le joueur 1 a gagné.')
    elif grille[0][0] == grille[0][1] == grille[0][2] == 'O' or grille[1][0] == grille[1][1] == grille[1][2] == 'O' or grille[2][0] == grille[2][1] == grille[2][2] == 'O' or grille[0][0] == grille[1][0] == grille[2][0] == 'O' or grille[0][1] == grille[1][1] == grille[1][2] == 'O' or grille[0][2] == grille[1][2] == grille[2][2] == 'O' or grille[0][0] == grille[1][1] == grille[2][2] == 'O' or grille[0][2] == grille[1][1] == grille[2][0] == 'O':
        print('Le joueur 2 a gagné.')
    else :
        pass


def grille_complete(grille):
    if " " in grille[0] or " " in grille[1] or " " in grille[2]:
        return False
    else:
        return True

def partie():
    joueur1 = input('Entrez le nom du joueur 1 : ') 
    joueur2 = input('Entrez le nom du joueur 2 : ')
    print(f'Bonjour {joueur1} et {joueur2}')
    while not grille_complete:
            afficher_grille(grille)
            jouer_coup_1(grille)
            afficher_grille(grille)
            if est_gagnee(grille):
                gagnant(grille)
                break
            jouer_coup_2(grille)
            if est_gagnee(grille):
                gagnant(grille)
                break       
    if not est_gagnee:
        print('Match nul.')
   

# partie()

afficher_grille(grille)
grille_complete(grille)
    
if not grille_complete(grille):
    print('ok')