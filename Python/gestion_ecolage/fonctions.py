import mois

def verification_matriule () :
    # L'utilisateur entre le matricule de la classe :
    matricule = input ("Entrer le matricule de la classe : \n exemple : info_2_2\n")
    
    # On n'a pu faire qu'une seule classe pour le moment :
    if matricule == 'info_2_2' :
        
        # Pour globaliser, si jamais dans le futur on a plus de matricules, on globalise dans ces variable :
        global etudiants_en_question
        global classe_en_question

        classe_en_question = mois.info_2_2
        etudiants_en_question = mois.etudiants_info_2_2

        entrer_nom ()

    # Dans le cas ou le matricule n'est pas enregistre, on la redemande :
    else : 
        print ("\nCe matricule n'existe pas. Verifiez bien l'orthographe.")
        verification_matriule ()

# Lister les etudiants dans la classe et demander lequel paye l'ecolage :
def entrer_nom () :
    print ("\nLes etudiants de cette classe sont : ")
    for x in classe_en_question :
        print (x)

    global nom_etudiant
    print ("\nSur lequel voulez-vous travailler ?\n entrer son prenom")
    nom_etudiant = input ('')

    payer ()

# Un eleve paye l'ecolage :
def payer () :

    x = 0
    
    # Parcourir les etudiants jusqu'a trouver celui cherche :
    while x != len (classe_en_question) : 

        if nom_etudiant == (classe_en_question [x]) :
            
            # Trouve !! :
            print ("\n" + classe_en_question [x] + " : ")

            # On affiche les mois payes :
            le_mois = 0
            for y in mois.liste_mois :
                print (mois.liste_mois [le_mois] + ' est : ' + etudiants_en_question [x] [le_mois])

                if etudiants_en_question [x] [le_mois] == 'non paye' :
                    print ("Le reste des mois suivent non payes.")
                    print ("\nVoulez-vous payer le mois de " + mois.liste_mois [le_mois] + " ?")
                    choix = input ('1. oui \n2. non\n')
                    
                    # L'etudiant paye l'ecolage :
                    if choix == '1' :
                        print ("Bon.")
                        etudiants_en_question [x] [le_mois] = 'paye'
                        print ("Le mois de " + mois.liste_mois [le_mois] + " de " + classe_en_question [x] + " est bien enregistre paye.")

                        print ("\n" + classe_en_question [x] + " : ")

                        le_mois_2 = 0
                        
                        for z in mois.liste_mois :
                            print (mois.liste_mois [le_mois_2] + ' est : ' + etudiants_en_question [x] [le_mois_2])

                        
                            if etudiants_en_question [x] [le_mois_2] == 'non paye' :
                                break
                            le_mois_2 += 1

                    else :
                        print ("Tant pis.")

                    # On arrete quand on trouve un mois non paye :
                    break
                
                le_mois += 1

            # On arrete quand on trouve l'etudiant qui paye l'ecolage :
            break

        x += 1

    # Le nom est incorrect :
    if x == len (classe_en_question):
        print ("Ce prenom n'est pas inscrit ici.")
        print ("Verifier l'orthographe, les espaces, les majuscules... : \n")
        print ("Voulez-vous reentrer un prenom ?\n1. Oui\n2. Non")
        choix = input ('')

        if choix == '1' :
            entrer_nom ()
        
        else :
            print ("Merci.")
    
    recommencer_avec_un_autre_etudiant ()

# Travailler avec un nom CORRECT ou un autre etudiant :
def recommencer_avec_un_autre_etudiant () :
    print ("\nTravailler sur un autre etudiant ? \n1. Oui\n2. Non")
    recommencer = input ("")
    
    if recommencer == '1' :
        verification_matriule ()
    
    else :
        print ("Merci.")