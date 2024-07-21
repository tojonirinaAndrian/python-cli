def presentation () :
    nom_d_l_utilisateur = input ("Tout d'abord, comment vous appellez-vous ?\n")
    print ("\nMes salutations " + nom_d_l_utilisateur + ", laissez moi vous expliquer ce qu'on fait ici. \n")
    print ("""Le but de ce petit CLI est d'aider tout le monde dans le besoin :
1. a faire des calculs basiques (somme, soustraction, multiplication, moyenne, division)
2. a ranger/regrouper les noms des elements d'une liste selon leur premiere lettre (donc, dans l'ordre alphabetique)
""")
    print ("Ce programme ne vise pas de metier precis mais chacun l'utilise selon ses propres besoins.")

def action () :
    print ("\nQue voulez-vous faire ? ")
    global choix
    choix = int (input ("""1. Des calculs basiques
2. Ranger une liste
"""))