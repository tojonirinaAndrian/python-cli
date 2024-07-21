def calculatrice_globale () :
    print ("\nVous avez deux options : ")
    print ("1. entrer a la suite les nombres a travailler puis on vous donne les resultats des calculs")
    print ("2. entrer un chiffre, choisir le calcul a faire, entrer le second chiffre, faire un autre calcul avec le resultat ou non")

un_ou_deux = '\nAlors, 1 ou 2 ? : '

# si l'utilisateur choisi la 1ere option

def action_1 () :
    print ('\nNous allons calculer, entrer les chiffres :\n(Quand vous ne voulez plus rien ajouter, scannez 0)')

    # imitialisations :
    nb_elements = 0
    somme = 0
    resultat_multiplication = 1
    nombre = int (input ('le nombre : '))
    soustraction = nombre

    # les calculs :
    for x in range (500) :
        
        somme += nombre
        
        if nombre == 0 :
            continue
            break
        
        nb_elements += 1
        moyenne = somme / nb_elements

        resultat_multiplication = resultat_multiplication * nombre
        
        nombre = int (input ('le nombre : '))
        
        soustraction -= nombre

    print ('\nLes resultats :')
    print ("La somme est : " + str (somme))
    print ("Le resultat des soustractions est : " + str (soustraction))
    print ("Le resultat des multiplications est : " + str (resultat_multiplication))
    print ("La moyenne est : " + str (moyenne))


# si l'utilisateur choisi la 2eme option 

def action_2 (a) :    

    choix = input ("+, -, *, /, lequel ? : \n")
    
    if choix == '+' :
        somme (a)
        choix = input ("Continuer ? 1.oui 2.non : \n")
    
        if choix == '1' :
            Continuer (resultat)
    
        else :
            print ("\nLe resultat final est : " + str (resultat))
    
    elif choix == '-' :
        soustraction (a) 
        choix = input ("\nContinuer ? 1.oui 2.non\n")
    
        if choix == '1' :
            Continuer (resultat)
    
        else :
            print ("")
    
    elif choix == '*' :
        multiplication (a) 
        choix = input ("\nContinuer ? 1.oui 2.non\n")
    
        if choix == '1' :
            Continuer (resultat)
    
        else :
            print ("")
    
    elif choix == "/" :
        division (a) 
        choix = input ("Continuer ? 1.oui 2.non\n")
    
        if choix == '1' :
            Continuer (resultat)
    
        else :
            print ("")
    
    else : 
        action_2 (a) 

# fonction pour continuer ou non le calcul :

def Continuer (resultat) :
    choix = input ("\nAvec le resultat comme chiffre initial ?\n1. Oui 2. Non\n: ")
    print ('')
    if choix == '1' :
        global a
        a = resultat
        print ("\na = " + str (a))
        action_2 (a)
    
    else :
        a = int (input ('a = '))
        action_2 (a)
    
# Les fonctions de calculs :

def somme (a) :
    b = int (input ('b = '))
    global resultat
    resultat = a + b
    print (str (a) + ' + ' + str (b) + " = " + str (resultat))

def soustraction (a) :
    b = int (input ('b = '))
    global resultat
    resultat = a - b
    print (str (a) + ' - ' + str (b) + " = " + str (resultat))

def multiplication (a) :
    b = int (input ('b = '))
    global resultat
    resultat = a * b
    print (str (a) + ' * ' + str (b) + " = " + str (resultat))

def division (a) :
    b = int (input ('b = '))
    
    if b == 0 :
        print ("impossible")
        division (a)
    
    else :
        global resultat
        resultat = a / b
        print (str (a) + ' / ' + str (b) + " = " + str (resultat))